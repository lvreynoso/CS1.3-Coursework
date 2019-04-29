#!python

from circularbuffer import CircularBuffer
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class CircularBufferTest(unittest.TestCase):

    def test_init(self):
        cb = CircularBuffer(8)
        assert cb.size == 0
        assert len(cb) == 8