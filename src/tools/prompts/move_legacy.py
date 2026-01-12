#!/usr/bin/env python3
"""Move duplicate prompt files to legacy folder."""
import os
import shutil

src_dir = os.path.dirname(os.path.abspath(__file__))
legacy_dir = os.path.join(src_dir, 'legacy')

# Create legacy directory
os.makedirs(legacy_dir, exist_ok=True)

# Files to move (duplicates of English modules)
to_move = [
    '敵対的レビュー凸.md',
    'コード監査凸.md', 
    'コード外科手術凹.md',
    'プロンプト構造監査凸.md',
    'プロンプト外科手術凹.md', 
    'システム構造監査.md',
    'リバースエンジニアリング.md',
    '第一原理思考.md',
    '発散と収束.md',
    '外科的再構築凹.md',
    'オッカムのカミソリ.md',
    '二次影響予測.md',
    '単純性原理と平易な説明.md'
]

moved = []
errors = []

for f in to_move:
    src = os.path.join(src_dir, f)
    dst = os.path.join(legacy_dir, f)
    if os.path.exists(src):
        try:
            shutil.move(src, dst)
            moved.append(f)
        except Exception as e:
            errors.append(f"{f}: {e}")
    else:
        errors.append(f"{f}: Not found")

print(f"Moved: {len(moved)} files")
for f in moved:
    print(f"  ✓ {f}")

if errors:
    print(f"\nErrors: {len(errors)}")
    for e in errors:
        print(f"  ✗ {e}")
