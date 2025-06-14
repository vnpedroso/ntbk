
from ntbk.utils.constants import NTBK_HOME

def ensure_ntbk_home() -> None:
    """Creates notebook base directory at users $HOME if it does not exist"""

    if not NTBK_HOME.exists():
        NTBK_HOME.mkdir(exist_ok=True)