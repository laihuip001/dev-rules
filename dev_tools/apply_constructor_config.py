import os
import shutil
from pathlib import Path

def apply_config():
    """
    Constructor環境（作業小屋）用の設定ファイルを適用します。
    Applies configuration files for the Constructor environment.
    """
    # 現在のディレクトリ（プロジェクトルートと想定）
    base_dir = Path(__file__).parent.parent.resolve()
    
    # ソース（設定ファイルの置き場所）
    source_dir = base_dir / "dev_tools" / "constructor_config"
    
    # ターゲット（適用先）
    antigravity_dir = base_dir / ".antigravity"
    vscode_dir = base_dir / ".vscode"
    
    # 1. .antigravity/rules.md の適用
    if not antigravity_dir.exists():
        antigravity_dir.mkdir(parents=True)
        print(f"作成しました: {antigravity_dir}")
        
    src_rules = source_dir / "rules.md"
    dst_rules = antigravity_dir / "rules.md"
    
    if src_rules.exists():
        shutil.copy2(src_rules, dst_rules)
        print(f"コピーしました: {src_rules.name} -> {dst_rules}")
    else:
        print(f"エラー: 元ファイルが見つかりません: {src_rules}")

    # 2. .vscode/settings.json の適用
    if not vscode_dir.exists():
        vscode_dir.mkdir(parents=True)
        print(f"作成しました: {vscode_dir}")
        
    src_settings = source_dir / "settings.json"
    dst_settings = vscode_dir / "settings.json"
    
    if src_settings.exists():
        shutil.copy2(src_settings, dst_settings)
        print(f"コピーしました: {src_settings.name} -> {dst_settings}")
    else:
        print(f"エラー: 元ファイルが見つかりません: {src_settings}")

    print("\n✅ Constructor環境の設定完了。")
    print("これで「大工役」として働く準備が整いました。")

if __name__ == "__main__":
    apply_config()
