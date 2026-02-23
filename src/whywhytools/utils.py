import os
from pathlib import Path
from typing import Union

def create_parent_dir(file: Union[str, Path]) -> None:
    """Ensure the parent directory of a file exists."""
    dir_path = os.path.dirname(file)
    if dir_path != '':
        os.makedirs(dir_path, exist_ok=True)
