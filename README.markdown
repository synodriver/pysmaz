<h1 align="center"><i>✨ Pysmaz ✨ </i></h1>

<h3 align="center">The python binding for <a href="https://github.com/antirez/smaz">smaz</a> </h3>

[![pypi](https://img.shields.io/pypi/v/python-smaz.svg)](https://pypi.org/project/python-smaz/)
![python](https://img.shields.io/pypi/pyversions/python-smaz)
![implementation](https://img.shields.io/pypi/implementation/python-smaz)
![wheel](https://img.shields.io/pypi/wheel/python-smaz)
![license](https://img.shields.io/github/license/synodriver/pysmaz.svg)
![action](https://img.shields.io/github/workflow/status/synodriver/pysmaz/build%20wheel)

### 安装

```
pip install python-smaz
```

###  usage
```python
import pysmaz

def compress(data: bytes, output_size: int = ...) -> bytes: ...
def decompress(data: bytes, output_size: int = ...) -> bytes: ...
def compress_into(data: bytes, output: bytearray) -> int: ...
def decompress_into(data: bytes, output: bytearray) -> int: ...
```

### 本机编译
```
python -m pip install setuptools wheel cython cffi
git clone https://github.com/synodriver/pysmaz
cd pysmaz
git submodule update --init --recursive
python setup.py bdist_wheel --use-cython --use-cffi
```

### 后端选择
默认由py实现决定，在cpython上自动选择cython后端，在pypy上自动选择cffi后端，使用```SMAZ_USE_CFFI```环境变量可以强制选择cffi