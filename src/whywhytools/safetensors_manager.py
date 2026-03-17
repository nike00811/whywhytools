"""This module provides utility functions for managing PyTorch files."""

import os
import sys
from pathlib import Path
from typing import Any



from .type_checker import check_type
from .utils import create_parent_dirs


def load_safetensors(file: str | Path, device: str | int = "cpu") -> Any:
    """
    Read a PyTorch file and return the loaded object.

    Args:
        file (Union[str, Path]): The path to the PyTorch file.
        map_location (Any, optional): A function, torch.device, string or a dict specifying how to remap storage locations.
        **kwargs: Additional keyword arguments to pass to torch.load.

    Returns:
        Any: The object read from the PyTorch file.
    """
    check_type(file, (str, Path))
    check_type(device, (str, int))

    from safetensors.torch import load_file

    return load_file(file, device=device)


def save_safetensors(
    obj: Any,
    file: str | Path,
    metadata: dict[str, str] | None = None,
    force: bool = False,
    silent: bool = False,
    raise_on_exists: bool = False,
) -> None:
    """
    Write an object to a PyTorch file.

    Args:
        obj (Any): The object to write to the file.
        file (Union[str, Path]): The path to the output PyTorch file.
        metadata (dict[str, str] | None, optional): Optional text only metadata you might want to save in your header.
            For instance it can be useful to specify more about the underlying
            tensors. This is purely informative and does not affect tensor loading.
        force (bool, optional): If True, overwrite the file if it exists. Defaults to False.
        silent (bool, optional): If True, suppress print messages. Defaults to False.
        raise_on_exists (bool, optional): If True, raise FileExistsError with full
            traceback instead of exiting cleanly. Defaults to False.

    Raises:
        FileExistsError: If the file exists, force is False, and raise_on_exists is True.
    """
    check_type(file, (str, Path))
    if os.path.exists(file) and not force:
        msg = f"[ERROR] {file} already exists."
        if raise_on_exists:
            raise FileExistsError(msg)
        sys.exit(msg)  # exit 1
    create_parent_dirs(file)

    from safetensors.torch import save_file

    save_file(obj, file, metadata=metadata)

    if not silent:
        print(f"[INFO] save to {file}")
