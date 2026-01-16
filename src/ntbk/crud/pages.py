from pathlib import Path

from ntbk.utils.constants import NTBK_HOME
from ntbk.utils.utils import treat_input, build_ntbk_path

def ensure_ntbk_page(pg_name: str) -> None:
    """creates notebook page if it does not exist

    Args:
        pg_name (str): the name of the notebook page
    """

    pg: Path = build_ntbk_path(pg_name)
    
    if not pg.exists():
        pg.touch()


