from pathlib import Path

from ntbk.utils.constants import NTBK_HOME, SEPARATOR
from ntbk.utils.utils import treat_input, build_ntbk_path, tabulate

def ensure_ntbk_page(pg_name: str) -> None:
    """creates notebook page if it does not exist

    Args:
        pg_name (str): the name of the notebook page
    """

    pg: Path = build_ntbk_path(pg_name)
    
    if not pg.exists():
        pg.touch()

def is_page_blank(fpage: Path) -> bool:
    """checks if the note's page is blank

    Args:
        fpage (Path): full path to page

    Returns:
        bool: True if the page is blank, or false if not
    """
    with open(fpage, mode="r") as f:
        first_char = f.read(3)

    return False if first_char else True


def read_page(fpage: Path, page_name: str) -> None:
    """displays all notes in a page

    Args:
        fpage (Path): the full path to the page
        page_name (str): the page name
    """

    headers = ["id","created_at","content"]
    rows = []

    with open(fpage, mode="r") as f:
        for line in f:
            row = line.strip("\n").split(SEPARATOR)
            rows.append(row)

    tabulate(
        title=page_name,
        headers=headers,
        rows=rows
    )
