from dataclasses import asdict, dataclass
from typing import Any

# ============================================================
# Living Sample: DTO (Data Transfer Object)
# ============================================================
# Imitation Points (G-6: Style Protocol):
# 1. @dataclass(frozen=True) : 不変オブジェクトとして定義
# 2. Type Hints : 全フィールドに型を明記 (Any禁止)
# 3. Factory Method : from_dict() で安全に生成
# ============================================================

@dataclass(frozen=True)
class UserDTO:
    """ユーザー情報を転送するための不変オブジェクト。

    Attributes:
        user_id: ユーザーの一意なID。
        name: 表示名。
        email: メールアドレス（オプション）。
        is_active: 有効なユーザーかどうか。
    """
    user_id: str
    name: str
    is_active: bool = True
    email: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "UserDTO":
        """辞書からDTOを生成するファクトリメソッド。

        余計なキーは無視し、型変換を行う場所としても機能する。

        Args:
            data: APIレスポンスなどの辞書データ。

        Returns:
            UserDTO: 検証済みのDTO。

        Raises:
            KeyError: 必須フィールドが欠けている場合。
        """
        return cls(
            user_id=str(data["user_id"]),
            name=str(data["name"]),
            is_active=bool(data.get("is_active", True)),
            email=data.get("email")  # OptionalなのでNone許容
        )

    def to_dict(self) -> dict[str, Any]:
        """辞書形式に変換する。"""
        return asdict(self)
