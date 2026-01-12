#!/usr/bin/env python3
"""Add YAML frontmatter to JP prompt files."""
import os
from pathlib import Path

PROMPTS_DIR = Path(r"c:\Users\makaron8426\開発(maka)\dev-rules\prompts")

# Mapping: filename -> id
FRONTMATTER_MAP = {
    "WBSスケジューリング.md": {
        "id": "JP-E1",
        "description": "戦術的実行計画とWBS分解",
        "alias": "E-1"
    },
    "エレガンススマート監査.md": {
        "id": "JP-Q4",
        "description": "美学的エレガンス監査",
        "alias": "Q-4"
    },
    "コンテキストの言語化.md": {
        "id": "JP-A7",
        "description": "暗黙の文脈を明文化",
        "alias": "A-7"
    },
    "コンテキスト構造化.md": {
        "id": "JP-B3",
        "description": "文脈の構造化と地図作成",
        "alias": "B-3"
    },
    "コーディング仕様書コンパイル.md": {
        "id": "JP-M1",
        "description": "エージェント向け仕様書コンパイル",
        "alias": "M-1"
    },
    "外部文脈の結合.md": {
        "id": "JP-I1",
        "description": "外部コンテキストの統合",
        "alias": "I-1"
    },
    "多角的ラテラル・シンキング.md": {
        "id": "JP-A2",
        "description": "多角的視点からの発想",
        "alias": "A-2"
    },
    "形態素解析マトリクス.md": {
        "id": "JP-A8",
        "description": "形態素分析による問題分解",
        "alias": "A-8"
    },
    "未踏の改善点.md": {
        "id": "JP-Q5",
        "description": "見落とされた改善点の発掘",
        "alias": None
    },
}

def add_frontmatter(filepath: Path, meta: dict) -> bool:
    content = filepath.read_text(encoding="utf-8")
    
    # Skip if already has frontmatter
    if content.strip().startswith("---"):
        print(f"⏭️  Skip (already has frontmatter): {filepath.name}")
        return False
    
    # Build frontmatter
    fm_lines = ["---"]
    fm_lines.append(f'id: {meta["id"]}')
    fm_lines.append(f'description: "{meta["description"]}"')
    if meta.get("alias"):
        fm_lines.append(f'alias: {meta["alias"]}')
    fm_lines.append("---")
    fm_lines.append("")
    
    new_content = "\n".join(fm_lines) + content
    filepath.write_text(new_content, encoding="utf-8")
    print(f"✅ Updated: {filepath.name}")
    return True

def main():
    updated = 0
    for filename, meta in FRONTMATTER_MAP.items():
        filepath = PROMPTS_DIR / filename
        if filepath.exists():
            if add_frontmatter(filepath, meta):
                updated += 1
        else:
            print(f"❌ Not found: {filename}")
    
    print(f"\n📦 Total updated: {updated} files")

if __name__ == "__main__":
    main()
