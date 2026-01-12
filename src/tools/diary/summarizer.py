"""
Gemini要約モジュール

Git履歴をGemini APIで要約し、構造化された日記エントリを生成。
新しい google-genai SDK を使用。
"""

import os
import json
from typing import TypedDict

try:
    from google import genai
except ImportError:
    genai = None


class DiarySummary(TypedDict):
    summary: str
    file_changes: list[str]
    decisions: list[str]
    learnings: list[str]
    next_steps: list[str]


# System Prompt for diary generation
DIARY_SYSTEM_PROMPT = """あなたは開発者の作業日記を作成するアシスタントです。

与えられたGitコミット履歴から、以下の4つのセクションに分けて日記を作成してください：

1. **Summary（概要）**: 今日の作業内容を2-3文で要約
2. **File Changes（ファイル変更）**: 主要な変更ファイルとその内容を箇条書き
3. **Decisions（意思決定）**: コミットメッセージから読み取れる設計判断や選択
4. **Learnings（学び）**: 今日の作業から得られた知見や気づき

日本語で出力してください。
技術用語は正確に、ただし説明は簡潔に。
ポートフォリオとして第三者にも見せることを意識してください。

出力形式はJSON:
{
  "summary": "...",
  "file_changes": ["...", "..."],
  "decisions": ["...", "..."],
  "learnings": ["...", "..."],
  "next_steps": ["...", "..."]
}
"""


def summarize_commits(commits: list[dict], api_key: str | None = None) -> DiarySummary:
    """
    コミット履歴をGeminiで要約
    
    Args:
        commits: collector.pyから取得したコミット情報リスト
        api_key: Gemini API key（Noneの場合は環境変数から取得）
        
    Returns:
        構造化された日記サマリー
    """
    if genai is None:
        raise ImportError(
            "google-genai is required. "
            "Install with: pip install google-genai"
        )
    
    api_key = api_key or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is required")
    
    # 新しいSDKではClientオブジェクトを使用
    client = genai.Client(api_key=api_key)
    
    # コミット情報をテキスト化
    commits_text = _format_commits_for_prompt(commits)
    
    # プロンプトを結合
    full_prompt = f"{DIARY_SYSTEM_PROMPT}\n\n今日のコミット履歴:\n{commits_text}"
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=full_prompt,
        config={
            "response_mime_type": "application/json"
        }
    )
    
    try:
        result = json.loads(response.text)
        return DiarySummary(
            summary=result.get("summary", ""),
            file_changes=result.get("file_changes", []),
            decisions=result.get("decisions", []),
            learnings=result.get("learnings", []),
            next_steps=result.get("next_steps", [])
        )
    except json.JSONDecodeError:
        # JSON解析失敗時はフォールバック
        return DiarySummary(
            summary=response.text[:500],
            file_changes=[],
            decisions=[],
            learnings=[],
            next_steps=[]
        )


def _format_commits_for_prompt(commits: list[dict]) -> str:
    """コミットリストをプロンプト用テキストに変換"""
    lines = []
    for c in commits:
        repo_prefix = f"[{c.get('repo', 'unknown')}] " if c.get('repo') else ""
        lines.append(f"## Commit: {repo_prefix}{c['hash'][:7]}")
        lines.append(f"- Date: {c['date']}")
        lines.append(f"- Message: {c['message']}")
        if c.get("files"):
            lines.append("- Files:")
            for f in c["files"]:
                lines.append(f"  - [{f['status']}] {f['path']}")
        lines.append("")
    return "\n".join(lines)
