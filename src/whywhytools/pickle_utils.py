from pathlib import Path
from typing import Union
import os

import pickle
def load_pickle(file: Union[str, Path]):
    if not isinstance(file, str):
        raise TypeError("file must be str, got {}".format(type(file).__name__))

    with open(file, 'rb') as f:
        obj = pickle.load(f)
    return obj

def save_pickle(obj, file: Union[str, Path], force=False, silent=False):
    if not isinstance(file, str):
        raise TypeError("file must be str, got {}".format(type(file).__name__))

    if os.path.exists(file) and force == False:
        print('[INFO] {} already exists.'.format(file))
        return
    
    dir_path = os.path.dirname(file)
    if dir_path != '':
        os.makedirs(dir_path, exist_ok=True)
    
    with open(file, 'wb') as f:
        pickle.dump(obj, f)
    
    if not silent:
        print('[INFO] save to {}'.format(file))
