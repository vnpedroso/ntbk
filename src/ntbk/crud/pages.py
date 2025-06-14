from pathlib import Path

from ntbk.utils.constants import NTBK_HOME

def ensure_ntbk_page(pg_name: str) -> None:
    """creates notebook page if it doesn not exist

    Args:
        pg_name (str): the name of the notebook page
    """

    pg: Path = Path.home() / NTBK_HOME / pg_name.lower()
    if not pg.exists():
        pg.mkdir(parents=True, exist_ok=True)
        pg.touch()