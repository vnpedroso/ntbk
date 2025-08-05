from rich.console import Console
from rich.table import Table   

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


def tabulate(title: str, headers: list[str], rows: list[list]) -> None:
    """
    Prints a cool table with the inputted data

    Args:
        title (str): the title of the table
        headers (list[str]): a list containing the columns titles
        rows (list[list]): a list with all the data points of the table, each a list on its own
    """

    table = Table(title=title)

    for idx in range(1,len(headers)):
        assert len(rows[idx]) == len(rows[idx - 1]), f"row {idx} and {idx - 1} have different lengths!"

    assert len(headers) == len(rows[0]), f"column titles and rows are not matching"

    for idx in range(0, len(headers)):
        table.add_column(headers[idx], justify="right",no_wrap=True)

    for row in rows:
        table.add_row(*row)

    console = Console()
    console.print(table)


    



