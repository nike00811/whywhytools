import os
from pathlib import Path
from typing import Union

def create_parent_dirs(file: Union[str, Path]) -> None:
    """Ensure the parent directories of a file exist."""
    dir_path = os.path.dirname(file)
    if dir_path != '':
        os.makedirs(dir_path, exist_ok=True)
