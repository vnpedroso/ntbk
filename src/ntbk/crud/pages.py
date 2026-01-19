from pathlib import Path

from ntbk.utils.constants import HEADERS, NTBK_HOME, SEPARATOR
from ntbk.utils.utils import treat_input, build_ntbk_path, page_into_content_rows, tabulate

def ensure_ntbk_page(pg_name: str) -> None:
    """creates notebook page if it does not exist

    Args:
        pg_name (str): the name of the notebook page
    """

    pg: Path = build_ntbk_path(pg_name)
    
    if not pg.exists():
        pg.touch()


def read_page(fpage: Path, page_name: str, headers: list[str]) -> None:
    """displays all notes in a page

    Args:
        fpage (Path): the full path to the page
        page_name (str): the page name
    """

    rows = page_into_content_rows(fpage)

    tabulate(
        title=page_name,
        headers=headers,
        rows=rows
    )
