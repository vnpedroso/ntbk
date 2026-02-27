from datetime import datetime
from filelock import FileLock
from pathlib import Path

from ntbk.utils.constants import FILELOCK, TIMESTAMP_FMT, SEPARATOR

from ntbk.utils.utils import page_into_str_lines

def check_id_match_index(note_id: int, lines: list[str]) -> bool:
    """
    checks if the provided note id is within the list of notes length
    if yes, also checks if the note with the input id has the same value as index position

    Args:
        note_id (int): the id inputed by the user
        lines (list[str]): a list of 'lines', each a note on the page

    Returns:
        bool: True if all checks pass, False otherwise
    """
    if note_id <= len(lines):
        if note_id == int(lines[note_id].split(SEPARATOR)[0]):
            return True
    
    return False

def edit_note_by_id(note_id: int, fpage: Path, new_content: str) -> None:

    lines = page_into_str_lines(fpage)

    if not (check_id_match_index(note_id, lines)):
        raise IndexError(f"note with id {note_id} not found in this page")
        
    with FileLock(FILELOCK):
        with open(fpage, mode="w") as f:
            for idx, line in enumerate(lines):

                if idx == note_id:
                    create = line.split(SEPARATOR)[1]
                    mod = datetime.now().strftime(TIMESTAMP_FMT)
                    new_line = f"{str(note_id)}{SEPARATOR}{create}{SEPARATOR}{mod}{SEPARATOR}{new_content}\n"
                else:
                    new_line = line

                if idx == len(lines) - 1:
                    f.write(new_line.replace("\n",""))
                else:
                    f.write(new_line)
                    
            return


    return 

def delete_note_by_id(note_id: int, fpage: Path) -> None:
    """deletes a notebook note by its id

    Args:
        note_id (int): the note id provided by the user
        fpage (Path): full path to the page in question
    """

    lines = page_into_str_lines(fpage)

    if check_id_match_index(note_id,lines):
        lines.pop(note_id)
    else: 
        raise IndexError(f"note with id {note_id} not found in this page")
    
    with FileLock(FILELOCK):
        with open(fpage, mode="w") as f:
            for idx, line in enumerate(lines):
                note = line.split(SEPARATOR,1)[1]
                if idx == len(lines) - 1:
                    new_line = str(idx) + SEPARATOR + note.replace("\n","")
                else:
                    new_line = str(idx) + SEPARATOR + note
                f.write(new_line)
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