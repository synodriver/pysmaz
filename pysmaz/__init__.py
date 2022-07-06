"""
Copyright (c) 2008-2021 synodriver <synodriver@gmail.com>
"""
import os
import platform

impl = platform.python_implementation()


def _should_use_cffi() -> bool:
    ev = os.getenv("SMAZ_USE_CFFI")
    if ev is not None:
        return True
    if impl == "CPython":
        return False
    else:
        return True


if not _should_use_cffi():
    from pysmaz.backends.cython import *
else:
    from pysmaz.backends.cffi import *

__version__ = "0.1.0"
