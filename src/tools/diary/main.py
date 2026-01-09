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

from src.tools.diary.collector import get_today_commits
from src.tools.diary.summarizer import summarize_commits
from src.tools.diary.writer import write_diary
from src.tools.diary.publisher import publish_diary


def main():
    parser = argparse.ArgumentParser(
        description="Generate development diary from Git commits"
    )
    parser.add_argument(
        "--target-repo",
        type=str,
        default=".",
        help="Path to the target repository to analyze"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help="Output directory for diary files (default: <repo>/diary)"
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
    
    args = parser.parse_args()
    
    # Resolve paths
    repo_path = Path(args.target_repo).resolve()
    output_dir = Path(args.output_dir) if args.output_dir else repo_path / "diary"
    
    print(f"📚 Development Diary Generator")
    print(f"   Repository: {repo_path}")
    print(f"   Output: {output_dir}")
    print(f"   Date: {datetime.now().strftime('%Y-%m-%d')}")
    print()
    
    # Step 1: Collect commits
    print("🔍 Collecting today's commits...")
    try:
        commits = get_today_commits(repo_path)
    except Exception as e:
        print(f"❌ Failed to collect commits: {e}")
        sys.exit(1)
    
    if not commits:
        print("⚠️  No commits found for today. Nothing to summarize.")
        sys.exit(0)
    
    print(f"   Found {len(commits)} commit(s)")
    
    # Step 2: Summarize with Gemini
    print("🤖 Summarizing with Gemini...")
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
    
    # Step 4: Publish to Git
    print("📤 Publishing to Git...")
    try:
        result = publish_diary(repo_path, diary_path, dry_run=args.dry_run)
    except Exception as e:
        print(f"❌ Failed to publish: {e}")
        sys.exit(1)
    
    if result["push"]["success"]:
        print("✅ Diary published successfully!")
    else:
        print(f"⚠️  Publish result: {result}")
    
    print()
    print("🎉 Done!")


if __name__ == "__main__":
    main()
