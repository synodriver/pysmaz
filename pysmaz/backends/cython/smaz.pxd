# cython: language_level=3
# cython: cdivision=True
cdef extern from "smaz.h" nogil:
    int smaz_compress(char *in_, int inlen, char *out, int outlen)
    int smaz_decompress(char *in_, int inlen, char *out, int outlen)