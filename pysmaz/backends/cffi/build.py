import glob
import sys

from cffi import FFI

ffibuilder = FFI()
ffibuilder.cdef(
    """
int smaz_compress(char *in, int inlen, char *out, int outlen);
int smaz_decompress(char *in, int inlen, char *out, int outlen);
    """
)

source = """
#include "smaz.h"
"""

ffibuilder.set_source(
    "pysmaz.backends.cffi._smaz_cffi",
    source,
    sources=["./smaz/smaz.c"],
    include_dirs=["./smaz"],
)

if __name__ == "__main__":
    ffibuilder.compile()
