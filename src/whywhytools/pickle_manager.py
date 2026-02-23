from pathlib import Path
from typing import Union, Any
import os
import pickle
from .type_checker import check_type
from .utils import create_parent_dir

def load_pickle(file: Union[str, Path]) -> Any:
    """
    Load an object from a pickle file.

    Args:
        file (Union[str, Path]): The path to the pickle file.

    Returns:
        Any: The object loaded from the pickle file.
    """
    check_type(file, (str, Path))

    with open(file, 'rb') as f:
        obj = pickle.load(f)
    return obj

def save_pickle(obj, file: Union[str, Path], force=False, silent=False) -> None:
    """
    Save an object to a pickle file.

    Args:
        obj (Any): The object to save.
        file (Union[str, Path]): The path to the output pickle file.
        force (bool, optional): If True, overwrite the file if it exists. Defaults to False.
        silent (bool, optional): If True, suppress print messages. Defaults to False.
    """
    check_type(file, (str, Path))
    if os.path.exists(file) and force == False:
        print('[INFO] {} already exists.'.format(file))
        return
    create_parent_dir(file)
    
    with open(file, 'wb') as f:
        pickle.dump(obj, f)
    
    if not silent:
        print('[INFO] save to {}'.format(file))
