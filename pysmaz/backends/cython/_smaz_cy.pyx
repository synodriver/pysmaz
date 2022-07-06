# cython: language_level=3
# cython: cdivision=True
from cpython.bytes cimport PyBytes_AS_STRING, PyBytes_FromStringAndSize
from libc.stdint cimport uint8_t

from pysmaz.backends.cython.smaz cimport smaz_compress, smaz_decompress


cpdef inline bytes compress(const uint8_t[::1] data, Py_ssize_t output_size = 0):
    cdef Py_ssize_t input_len = data.shape[0]
    if output_size==0:
        output_size = input_len # 如果没有指定输出buffer的大小，默认就是2倍输入大小
    cdef bytes output = PyBytes_FromStringAndSize(NULL, output_size)
    if <void*>output == NULL:
        raise MemoryError
    cdef int buffer_updated
    cdef char *output_ptr = PyBytes_AS_STRING(output)
    with nogil:
        buffer_updated = smaz_compress(<char*>&data[0], <int>input_len, output_ptr, <int>output_size)
    if buffer_updated == <int>input_len+1:
        raise ValueError("output buffer is too small")
    
    return output[:buffer_updated]

cpdef inline bytes decompress(const uint8_t[::1] data, Py_ssize_t output_size = 0):
    cdef Py_ssize_t input_len = data.shape[0]
    if output_size==0:
        output_size = input_len * 2 # 如果没有指定输出buffer的大小，默认就是2倍输入大小
    
    cdef bytes output = PyBytes_FromStringAndSize(NULL, output_size)
    if <void*>output == NULL:
        raise MemoryError
    cdef int buffer_updated
    cdef char *output_ptr = PyBytes_AS_STRING(output)
    with nogil:
        buffer_updated = smaz_decompress(<char*>&data[0], <int>input_len, output_ptr, <int>output_size)
    if buffer_updated == <int>output_size+1:
        raise ValueError("output buffer is too small")

    return output[:buffer_updated]


cpdef inline int compress_into(const uint8_t[::1] data, uint8_t[::1] output) except *:
    cdef Py_ssize_t output_size = output.shape[0]
    cdef int ret
    with nogil:
        ret =  smaz_compress(<char *> &data[0], <int> data.shape[0], <char*>&output[0], <int>output_size)
    if ret == <int>output_size + 1:
        raise ValueError("output buffer is too small")
    return ret

cpdef inline int decompress_into(const uint8_t[::1] data, uint8_t[::1] output) except *:
    cdef Py_ssize_t output_size = output.shape[0]
    cdef int ret
    with nogil:
        ret =  smaz_decompress(<char *> &data[0], <int> data.shape[0], <char*>&output[0], <int>output_size)
    if ret == <int>output_size + 1:
        raise ValueError("output buffer is too small")
    return ret