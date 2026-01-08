
import os
import logging
from enum import Enum

class AppMode(Enum):
    PERSONAL = "PERSONAL"
    PUBLIC = "PUBLIC"

def get_app_mode() -> AppMode:
    mode_str = os.getenv("APP_MODE", "PERSONAL").upper()
    try:
        return AppMode(mode_str)
    except ValueError:
        logging.warning(f"Invalid APP_MODE '{mode_str}', falling back to PERSONAL")
        return AppMode.PERSONAL

def is_personal_mode() -> bool:
    return get_app_mode() == AppMode.PERSONAL

def is_public_mode() -> bool:
    return get_app_mode() == AppMode.PUBLIC
