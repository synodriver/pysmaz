"""
Copyright (c) 2008-2021 synodriver <synodriver@gmail.com>
"""
from pysmaz.backends.cffi._smaz_cffi import ffi, lib


def compress(data: bytes, output_size=0) -> bytes:
    input_len = len(data)
    if output_size == 0:
        output_size = input_len  # 如果没有指定输出buffer的大小，默认就是就是输入大小
    output = ffi.new(f"char[{output_size}]")

    buffer_updated: int = lib.smaz_compress(
        ffi.from_buffer(data), input_len, output, output_size
    )
    if buffer_updated == output_size + 1:
        raise ValueError("output buffer is too small")
    return ffi.unpack(output, buffer_updated)


def decompress(data: bytes, output_size=0) -> bytes:
    input_len = len(data)
    if output_size == 0:
        output_size = input_len * 2  # 如果没有指定输出buffer的大小，默认就是2倍输入大小
    output = ffi.new(f"char[{output_size}]")

    buffer_updated: int = lib.smaz_decompress(
        ffi.from_buffer(data), input_len, output, output_size
    )
    if buffer_updated == output_size + 1:
        raise ValueError("output buffer is too small")
    return ffi.unpack(output, buffer_updated)


def compress_into(data: bytes, output: bytearray) -> int:
    output_size = len(output)
    ret: int = lib.smaz_compress(
        ffi.from_buffer(data), len(data), ffi.from_buffer(output), output_size
    )
    if ret == output_size + 1:
        raise ValueError("output buffer is too small")
    return ret


def decompress_into(data: bytes, output: bytearray) -> int:
    output_size = len(output)
    ret: int = lib.smaz_decompress(
        ffi.from_buffer(data), len(data), ffi.from_buffer(output), output_size
    )
    if ret == output_size + 1:
        raise ValueError("output buffer is too small")
    return ret
