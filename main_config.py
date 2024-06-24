from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CORE_DIR = BASE_DIR / 'core'

FONT_FILE_PATH = CORE_DIR / 'fonts' / 'orange juice 2.0.ttf'
ICONS_DIR = CORE_DIR / 'icons'
AVATAR_DIR = CORE_DIR / 'avatar'
AVATAR_FILE_NAME = 'avatar.png'
GENERATED_AVATAR_PATH = AVATAR_DIR / AVATAR_FILE_NAME

DEBUG = True

CORE_DIRS = [AVATAR_DIR]
