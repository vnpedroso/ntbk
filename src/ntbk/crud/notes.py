from datetime import datetime
from filelock import FileLock
from pathlib import Path

from ntbk.utils.constants import FILELOCK, TIMESTAMP_FMT, SEPARATOR

from ntbk.utils.utils import page_into_str_lines

def check_id_match_index(note_id: int, lines: list[str]) -> bool:
    """_summary_

    Args:
        note_id (int): _description_
        liens (list[str]): _description_

    Returns:
        bool: _description_
    """
    if note_id <= len(lines):
        if note_id == int(lines[note_id].split(SEPARATOR)[0]):
            return True
    
    return False

def delete_note_by_id(note_id: int, fpage: Path) -> None:
    """_summary_

    Args:
        note_id (int): _description_
        fpage (Path): _description_

    Returns:
        _type_: _description_
    """

    lines = page_into_str_lines(fpage)

    if check_id_match_index(note_id,lines):
        lines.pop(note_id)
    else: 
        raise IndexError(f"note id {note_id} has no equivalent row")
    
    with FileLock(FILELOCK):
        with open(fpage, mode="w") as f:
            for li in lines:
                f.write(li)
            return

def write_note(note: str, overwrite: bool, fpage: Path) -> None:
    """writes note in its respective page

    Args:
        note (str): the note to be written
        overwrite (bool): if the note is to be appended or overwriten
        fpage (Path): full page to the note's page
    """

    with FileLock(FILELOCK):
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

    with FileLock(FILELOCK):
        with open(fpage, mode="r") as f:
            for line in f:
                pass
            last_line = line

    note_id = int(last_line.split(sep)[0])
    return note_id

def is_within_id_limit(note_id: int, max_notes_on_page: int) -> bool:
    """checks if NEXT note will violate the max note limit per page

    Args:
        note_id (int): id of the last note on the page

    Returns:
        bool: False if limit is violated, otherwise True
    """
    return True if note_id + 1 < max_notes_on_page else False
    

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
    note = f"{str(note_id)}{sep}{timestp}{sep}{timestp}{sep}{content}"
    return note