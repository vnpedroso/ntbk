from pathlib import Path

from ntbk.utils.constants import NTBK_HOME
from ntbk.utils.utils import treat_input

def ensure_ntbk_page(pg_name: str) -> None:
    """creates notebook page if it doesn not exist

    Args:
        pg_name (str): the name of the notebook page
    """

    pg_name = treat_input(pg_name)

    pg: Path = Path.home() / NTBK_HOME / f"{pg_name}.txt"
    if not pg.exists():
        pg.touch()

