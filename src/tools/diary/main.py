"""
開発日記生成ツール - メインエントリーポイント

使用方法:
    python -m src.tools.diary.main --target-repo "path/to/repo"
    python -m src.tools.diary.main --dry-run  # プッシュなしでテスト
"""

import argparse
import sys
import os
from pathlib import Path
from datetime import datetime

# Add parent to path for relative imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from src.tools.diary.collector import collect_commits_from_repos
from src.tools.diary.summarizer import summarize_commits
from src.tools.diary.writer import write_diary
from src.tools.diary.publisher import publish_diary


def main():
    parser = argparse.ArgumentParser(
        description="Generate development diary from Git commits"
    )
    parser.add_argument(
        "--target-repos",
        nargs="+",
        default=["."],
        help="Path(s) to target repositories to analyze"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help="Output directory for diary files (default: ./diary)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Don't push to remote, just generate locally"
    )
    parser.add_argument(
        "--api-key",
        type=str,
        default=None,
        help="Gemini API key (default: use GEMINI_API_KEY env var)"
    )
    parser.add_argument(
        "--skip-ai",
        action="store_true",
        help="Skip AI summarization, use raw git log as diary content"
    )
    
    args = parser.parse_args()
    
    # Resolve paths
    repo_paths = [Path(p).resolve() for p in args.target_repos]
    
    # 出力先は指定がなければカレントディレクトリ配下のdiary
    # 複数リポジトリの場合、特定のtarget_repoに依存させるのは危険なため、実行場所基準とする
    current_dir = Path.cwd()
    output_dir = Path(args.output_dir) if args.output_dir else current_dir / "diary"
    
    print(f"📚 Development Diary Generator")
    print(f"   Targets: {[p.name for p in repo_paths]}")
    print(f"   Output: {output_dir}")
    print(f"   Date: {datetime.now().strftime('%Y-%m-%d')}")
    print()
    
    # Step 1: Collect commits
    print("🔍 Collecting today's commits...")
    try:
        commits = collect_commits_from_repos(repo_paths)
    except Exception as e:
        print(f"❌ Failed to collect commits: {e}")
        sys.exit(1)
    
    if not commits:
        print("⚠️  No commits found for today in any repository. Nothing to summarize.")
        sys.exit(0)
    
    print(f"   Found {len(commits)} commit(s)")
    
    # Step 2: Summarize (with AI or fallback)
    if args.skip_ai:
        print("📋 Creating summary from Git log (AI skipped)...")
        summary = _create_fallback_summary(commits)
    else:
        print("🤖 Summarizing with Gemini...")
        print("   (This may take a moment...)")
        try:
            summary = summarize_commits(commits, api_key=args.api_key)
        except ImportError as e:
            print(f"❌ Missing dependency: {e}")
            sys.exit(1)
        except ValueError as e:
            print(f"❌ Configuration error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Summarization failed: {e}")
            sys.exit(1)
    
    print("   Summary generated!")
    
    # Step 3: Write diary file
    print("📝 Writing diary file...")
    try:
        diary_path = write_diary(summary, output_dir)
    except Exception as e:
        print(f"❌ Failed to write diary: {e}")
        sys.exit(1)
    
    print(f"   Created: {diary_path}")
    
    # Step 4: Publish to Git (to the repository containing output_dir)
    print("📤 Publishing to Git...")
    # output_dirを含むリポジトリを検出するのがベストだが、簡易的にカレントを採用
    publish_repo = current_dir
    
    try:
        result = publish_diary(publish_repo, diary_path, dry_run=args.dry_run)
    except Exception as e:
        print(f"❌ Failed to publish: {e}")
        sys.exit(1)
    
    if result["push"]["success"]:
        print("✅ Diary published successfully!")
    else:
        # Commitなし(変更なし)の場合等はここに来る
        if result["commit"] and not result["commit"]["success"]:
             # コミット失敗時
             pass
             
        print(f"⚠️  Publish result: {result}")
    
    print()
    print("🎉 Done!")


def _create_fallback_summary(commits: list) -> dict:
    """AI無しでGitログから基本的なサマリーを生成"""
    file_changes = []
    for c in commits:
        repo = c.get('repo', 'unknown')
        msg = c['message'][:50]
        for f in c.get("files", []):
            file_changes.append(f"[{repo}] [{f['status']}] {f['path']} ({msg})")
    
    decisions = [f"[{c.get('repo','?')}] {c['message']}" for c in commits]
    
    return {
        "summary": f"今日は{len(commits)}件のコミットを行いました。",
        "file_changes": file_changes,
        "decisions": decisions,
        "learnings": ["(AI要約をスキップしました)"],
        "next_steps": []
    }


if __name__ == "__main__":
    main()
