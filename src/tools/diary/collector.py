"""
Git履歴収集モジュール

当日のコミット履歴を収集し、構造化データとして返す。
"""

import subprocess
import json
from datetime import datetime
from pathlib import Path
from typing import TypedDict


class CommitInfo(TypedDict):
    hash: str
    repo: str
    author: str
    date: str
    message: str
    files: list[dict[str, str]]


def get_today_commits(repo_path: str | Path) -> list[CommitInfo]:
    """
    指定リポジトリの当日コミットを取得
    
    Args:
        repo_path: リポジトリのパス
        
    Returns:
        コミット情報のリスト
    """
    repo_path = Path(repo_path)
    repo_name = repo_path.name
    
    # 当日の開始時刻
    today = datetime.now().strftime("%Y-%m-%d 00:00:00")
    
    # git log コマンド（JSON風フォーマット）
    log_format = "--pretty=format:%H||%an||%ai||%s"
    
    result = subprocess.run(
        ["git", "log", f"--since={today}", log_format, "--name-status"],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    
    if result.returncode != 0:
        raise RuntimeError(f"git log failed: {result.stderr}")
    
    commits = _parse_git_log(result.stdout)
    
    # repo名を追加
    for c in commits:
        c["repo"] = repo_name
        
    return commits


def collect_commits_from_repos(repo_paths: list[Path]) -> list[CommitInfo]:
    """複数リポジトリからコミットを収集し、日時順にソート"""
    all_commits = []
    
    for path in repo_paths:
        try:
            commits = get_today_commits(path)
            all_commits.extend(commits)
        except Exception as e:
            print(f"⚠️ Failed to collect from {path}: {e}")
            continue
    
    # 日時順（新しい順）にソート
    # date string format: YYYY-MM-DD HH:MM:SS +TZ
    all_commits.sort(key=lambda x: x["date"], reverse=True)
    
    return all_commits


def _parse_git_log(raw_output: str) -> list[CommitInfo]:
    """git log出力をパースしてCommitInfoリストに変換"""
    commits = []
    current_commit = None
    
    for line in raw_output.strip().split("\n"):
        if not line:
            continue
            
        # コミット情報行（||で区切られている）
        if "||" in line:
            if current_commit:
                commits.append(current_commit)
            
            parts = line.split("||")
            if len(parts) >= 4:
                current_commit = CommitInfo(
                    hash=parts[0],
                    author=parts[1],
                    date=parts[2],
                    message=parts[3],
                    files=[]
                )
        # ファイル変更行（A/M/D + タブ + ファイル名）
        elif current_commit and "\t" in line:
            status, filepath = line.split("\t", 1)
            current_commit["files"].append({
                "status": _status_to_label(status),
                "path": filepath
            })
    
    if current_commit:
        commits.append(current_commit)
    
    return commits


def _status_to_label(status: str) -> str:
    """Gitステータスコードをラベルに変換"""
    mapping = {
        "A": "Added",
        "M": "Modified",
        "D": "Deleted",
        "R": "Renamed",
        "C": "Copied"
    }
    return mapping.get(status, status)


if __name__ == "__main__":
    # テスト用
    import sys
    repo = sys.argv[1] if len(sys.argv) > 1 else "."
    commits = get_today_commits(repo)
    print(json.dumps(commits, indent=2, ensure_ascii=False))
