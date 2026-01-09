"""
Git自動パブリッシャー

日記ファイルをGitで自動コミット・プッシュ。
"""

import subprocess
from pathlib import Path
from datetime import datetime


def publish_diary(
    repo_path: str | Path,
    diary_file: str | Path,
    dry_run: bool = False
) -> dict:
    """
    日記ファイルをGitでコミット・プッシュ
    
    Args:
        repo_path: リポジトリのパス
        diary_file: 日記ファイルのパス
        dry_run: Trueの場合は実際にプッシュしない
        
    Returns:
        実行結果の辞書
    """
    repo_path = Path(repo_path)
    diary_file = Path(diary_file)
    
    # diary_fileの相対パスを取得
    try:
        relative_path = diary_file.relative_to(repo_path)
    except ValueError:
        relative_path = diary_file
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    commit_message = f"[Diary] Add dev diary for {date_str}"
    
    results = {
        "add": None,
        "commit": None,
        "push": None,
        "dry_run": dry_run
    }
    
    # git add
    add_result = subprocess.run(
        ["git", "add", str(relative_path)],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    results["add"] = {
        "success": add_result.returncode == 0,
        "output": add_result.stdout or add_result.stderr
    }
    
    if add_result.returncode != 0:
        return results
    
    # git commit
    commit_result = subprocess.run(
        ["git", "commit", "-m", commit_message],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    results["commit"] = {
        "success": commit_result.returncode == 0,
        "output": commit_result.stdout or commit_result.stderr
    }
    
    if commit_result.returncode != 0:
        return results
    
    # git push (skip if dry_run)
    if dry_run:
        results["push"] = {"success": True, "output": "[DRY RUN] Push skipped"}
        return results
    
    push_result = subprocess.run(
        ["git", "push", "origin", "HEAD"],
        cwd=repo_path,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    results["push"] = {
        "success": push_result.returncode == 0,
        "output": push_result.stdout or push_result.stderr
    }
    
    return results
