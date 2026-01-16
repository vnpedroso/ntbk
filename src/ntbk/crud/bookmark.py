from pathlib import Path

from ntbk.utils.constants import BOOKMARK
from ntbk.utils.utils import treat_input

def ensure_bookmark() -> None:
    """creates bookmark file if it does not exists"""

    if not BOOKMARK.exists():
        BOOKMARK.touch()

def read_bookmark() -> str:
    """reads the contents of the bookmarked file

    Returns:
        str: current 'bookmarked' page 
    """

    return BOOKMARK.read_text()

def write_bookmark(new_bmk: str) -> None:
    """writes a page to the bookmark file

    Args:
        new_bmk (str): page name to bookmark
    """
    new_bmk = treat_input(new_bmk)
    BOOKMARK.write_text(new_bmk)
