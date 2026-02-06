from pathlib import Path

NTBK_HOME: Path = Path.home() / ".ntbk"
BOOKMARK: Path = Path.home() / NTBK_HOME / "bookmark.txt"
SEPARATOR: str = "::"
TIMESTAMP_FMT: str = "%d/%m/%Y %H:%M"
HEADERS: list[str] = ["id", "created_at", "content"]
FILELOCK: Path = NTBK_HOME / "ntbk.lock"
PAGE_MAX_NOTES: int = 100

