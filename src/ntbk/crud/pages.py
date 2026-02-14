from pathlib import Path

from ntbk.utils.constants import NTBK_HOME

from ntbk.utils.utils import (
    build_ntbk_path,
    page_into_content_rows,
    tabulate,
)


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

    tabulate(title=page_name, headers=headers, rows=rows)


def list_pages(ntbk_home: Path) -> list[str]:
    """Returns a list of all page files

    Returns:
        list[str]: a list of all '.txt' files within ntbk home dir
    """
    return [
        i.name.replace(".txt", "")
        for i in list(ntbk_home.glob("*.txt"))
        if i.name.replace(".txt", "") != "bookmark"
    ]

def empty_notebook(page: str, bmk_page: str) -> bool:
    """checks if a single page was created in the notebook

    Args:
        page (str): name of the page, usually a provided arg or option
        bmk_page (str): the current bookmarked page

    Returns:
        bool: True if the notebook is empty, False otherwise
    """
    return True if not (page or bmk_page) else False

def input_page_or_bmk(page: str, bmk: str) -> tuple[str, Path]:
    """checks if the program will use the inputed page or the bookmark page

    Args:
        page (str): inputed page by the user, if any
        bmk (str): current bookmark page


    Returns:
        tuple[str, Path]: tuple made of the used page and its full path
    """

    if page:
        return page, build_ntbk_path(page)
    
    return bmk, build_ntbk_path(bmk)

def page_exists(page: str) -> bool:
    """checks if page exists

    Args:
        page (str): name of the inputed page

    Returns:
        bool: True if page exists, False otherwise
    """
    return True if page in list_pages(NTBK_HOME) else False