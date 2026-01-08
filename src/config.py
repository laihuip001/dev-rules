import os
from pathlib import Path

# ============================================================
# Living Sample: Configuration Management
# ============================================================
# Imitation Points (G-6: Style Protocol):
# 1. os.environ.get : 環境変数の安全な取得 (フォールバック付)
# 2. pathlib.Path : ファイルパスのモダンな操作
# 3. Type Hints : 戻り値の型を明記
# ============================================================

class AppConfig:
    """アプリケーション設定を管理するクラス。"""

    def __init__(self) -> None:
        """設定を初期化する。

        環境変数から値を読み込み、デフォルト値を適用する。
        """
        # 環境変数から読み込み、デフォルト値を設定
        self.env: str = os.environ.get("APP_ENV", "development")
        self.debug: bool = os.environ.get("APP_DEBUG", "false").lower() == "true"
        self.port: int = int(os.environ.get("APP_PORT", "8080"))

        # パス操作には pathlib を使用
        self.root_dir: Path = Path(__file__).parent.parent
        self.data_dir: Path = self.root_dir / "data"

    def get_database_url(self) -> str:
        """データベース接続URLを取得する。

        Returns:
            str: 接続文字列。
        """
        # 必須環境変数は取得時にチェックしても良い
        db_url = os.environ.get("DATABASE_URL")
        if not db_url:
            # 開発環境ならデフォルト値を返すフォールバック戦略
            if self.env == "development":
                return "sqlite:///./dev.db"
            raise ValueError("DATABASE_URL is not set in production environment")
        return db_url

# シングルトンとしてインスタンス化
config = AppConfig()
