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
        assert cb.is_empty() == True

    def test_enqueue(self):
        cb = CircularBuffer(4)
        cb.enqueue(3)
        assert cb.size == 1
        assert len(cb) == 4
        assert cb.is_empty() == False
        cb.enqueue(1)
        assert cb.size == 2
        cb.enqueue(4)
        assert cb.size == 3
        cb.enqueue(1)
        assert cb.size == 4
        assert cb.is_full() == True
        cb.enqueue(5)
        assert cb.size == 4

    def test_front(self):
        cb = CircularBuffer(4)
        cb.enqueue(3)
        assert cb.front() == 3
        cb.enqueue(1)
        assert cb.front() == 3
        cb.enqueue(4)
        assert cb.front() == 3
        cb.enqueue(1)
        assert cb.front() == 3
        cb.enqueue(5)
        assert cb.front() == 1

    def test_dequeue(self):
        cb = CircularBuffer(4)
        cb.enqueue(3)
        cb.enqueue(1)
        cb.enqueue(4)
        cb.enqueue(1)
        assert cb.dequeue() == 3
        assert cb.dequeue() == 1
        assert cb.dequeue() == 4
        assert cb.dequeue() == 1

    def test_overflow(self):
        cb = CircularBuffer(4)
        cb.enqueue(3)
        cb.enqueue(1)
        cb.enqueue(4)
        cb.enqueue(1)
        assert cb.front() == 3
        cb.enqueue(5)
        assert cb.front() == 1
        assert cb.dequeue() == 1

if __name__ == '__main__':
    unittest.main()