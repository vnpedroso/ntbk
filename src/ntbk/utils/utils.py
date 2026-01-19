
from pathlib import Path
from rich.console import Console
from rich.table import Table

from ntbk.utils.constants import NTBK_HOME, SEPARATOR

def build_ntbk_path(fname: str) -> Path:
    """
    generates the full path to the file

    Args:
        fname (str): the name of the file

    Returns:
        Path: the Path object of the page
    """

    fname = treat_input(fname)
    return Path.home() / NTBK_HOME / f"{fname}.txt"

def treat_input(text: str) -> str:
    """
    Treats the input text by removing leading and trailing whitespace,
    replacing multiple spaces into a single underscore, and ensuring lowercase.
    
    Args:
        text (str): The input text to be treated.
        
    Returns:
        str: The treated text.
    """

    return '_'.join(text.strip().split()).lower()


def tabulate(title: str, headers: list[str], rows: list[list[str]]) -> None:
    """
    Prints a cool table with the inputted data

    Args:
        title (str): the title of the table
        headers (list[str]): a list containing the columns titles
        rows (list[list[str]]): a list with all the data points of the table, each a list on its own
    """

    table = Table(title=title)

    for row in rows:
        assert len(row) == len(headers), "headers and all content rows must have same length!"

    assert len(headers) == len(rows[0]), "column titles and rows are not matching"

    for idx in range(0, len(headers)):
        table.add_column(headers[idx], justify="right",no_wrap=True)

    for row in rows:
        table.add_row(*row)

    console = Console()
    console.print(table)


def is_page_blank(fpage: Path) -> bool:
    """
    checks if the note's page is blank

    Args:
        fpage (Path): full path to page

    Returns:
        bool: True if the page is blank, or false if not
    """
    with open(fpage, mode="r") as f:
        first_char = f.read(3)

    return False if first_char else True


def page_into_content_rows(fpage: Path) -> list[list[str]]:
    """
    reads a page file into a 'rows' of content

    Args:
        fpage (Path): full path to the page file

    Returns:
        list[list[str]]: the content 'rows'
    """

    rows = []

    with open(fpage, mode="r") as f:
        for line in f:
            row = line.strip("\n").split(SEPARATOR)
            rows.append(row)

    return rows



