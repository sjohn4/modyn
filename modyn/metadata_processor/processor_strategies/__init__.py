"""This module contains extensions of the MetadataProcessorStrategy class that
implement custom processing strategies."""

import os

files = os.listdir(os.path.dirname(__file__))
files.remove("__init__.py")
__all__ = [f[:-3] for f in files if f.endswith(".py")]
