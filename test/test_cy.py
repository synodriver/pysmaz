"""
Copyright (c) 2008-2021 synodriver <synodriver@gmail.com>
"""
import sys
from random import choice, randint
from unittest import TestCase

sys.path.append("..")

from pysmaz import compress, decompress


class TestAll(TestCase):
    def setUp(self) -> None:
        pass

    def test_raise(self):
        with self.assertRaises(ValueError):
            compress(b"1234")

    def test_encode(self):
        for i in range(1000):
            data = bytes([randint(0, 255) for _ in range(randint(100, 1000))])
            out = compress(data, 3000)
            self.assertEqual(decompress(out, 2000), data)
        pass

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    import unittest

    unittest.main()
