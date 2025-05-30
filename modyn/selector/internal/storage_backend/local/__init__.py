"""This submodule provides a backend for storing the seen samples to local
storage during a pipeline."""

import os

from .local_storage_backend import LocalStorageBackend  # noqa: F401

files = os.listdir(os.path.dirname(__file__))
files.remove("__init__.py")
__all__ = [f[:-3] for f in files if f.endswith(".py")]
