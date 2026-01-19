from datetime import datetime
from pathlib import Path

from ntbk.utils.constants import TIMESTAMP_FMT

def is_within_char_limit(content: str) -> bool:
    """checks if note is complying to 144 char limit

    Args:
        content (str): content of the note to be written

    Returns:
        bool: True if note is within 144 char limit, else False
    """

    return False if len(content) > 144 else True


def write_note(note: str, overwrite: bool, fpage: Path) -> None:
    """writes note in its respective page

    Args:
        note (str): the note to be written
        overwrite (bool): if the note is to be appended or overwriten
        fpage (Path): full page to the note's page
    """

    if overwrite:
        with open(fpage, mode="w") as f:
            f.write(note)
            return
        
    with open(fpage, mode="a") as f:
        f.write("\n" + note)
        return




def get_last_note_id(fpage: Path, sep: str) -> int:
    """retrieves the id of the last note in page

    Args:
        fpage (Path): full path to the note's page
        sep (str): separator being used in the note

    Returns:
        int: integer value of the note id
    """

    with open(fpage, mode="r") as f:
        for line in f:
            pass
        last_line = line

    note_id = int(last_line.split(sep)[0])
    return note_id
    

def format_content(content: str, note_id: int, sep: str) -> str:
    """formats the note content, 
        adding a valid id and a creation/modificaiton timestamp

    Args:
        content (str): the content of the note
        note_id (int): id value for the note
        sep (str): separator being used in the note

    Returns:
        str: the fully formated note
    """

    timestp = datetime.now().strftime(TIMESTAMP_FMT)
    note = f"{str(note_id)}{sep}{timestp}{sep}{content}"
    return note