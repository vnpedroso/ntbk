from pathlib import Path


def is_within_char_limit(note: str) -> bool:
    """checks if note is complying to 144 char limit

    Args:
        note (str): note to be written

    Returns:
        bool: True if note is within 144 char limit, else False
    """

    return False if len(note) > 144 else True


def write_note(note: str, append: bool, fpage: Path) -> None:
    """writes note in its respective page

    Args:
        note (str): the note to be written
        append (bool): if the note is to be appended or written
        fpage (Path): full page to the note's page
    """

    if append:
        with open(fpage, mode="a") as f:
            f.write(note)
            return
    
    with open(fpage, mode="w") as f:
        f.write("\n" + note)
        return



