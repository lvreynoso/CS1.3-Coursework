#!python

from deque import Deque
import unittest

class DequeTest(unittest.TestCase):

    def test_init(self):
        d = Deque()
        assert d.front() is None
        assert d.length() == 0
        assert d.is_empty() is True

    def test_init_with_list(self):
        d = Deque(['A', 'B', 'C'])
        assert d.front() == 'A'
        assert d.length() == 3
        assert d.is_empty() is False

    def test_length(self):
        d = Deque()
        assert d.length() == 0
        d.push_back('A')
        assert d.length() == 1
        d.push_back('B')
        assert d.length() == 2
        d.pop_front()
        assert d.length() == 1
        d.pop_front()
        assert d.length() == 0

    def test_push_back(self):
        d = Deque()
        d.push_back('A')
        assert d.front() == 'A'
        assert d.length() == 1
        d.push_back('B')
        assert d.front() == 'A'
        assert d.length() == 2
        d.push_back('C')
        assert d.front() == 'A'
        assert d.length() == 3
        assert d.is_empty() is False

    def test_push_front(self):
        d = Deque()
        d.push_front('A')
        assert d.front() == 'A'
        assert d.length() == 1
        d.push_front('B')
        assert d.front() == 'B'
        assert d.length() == 2
        d.push_front('C')
        assert d.front() == 'C'
        assert d.length() == 3
        assert d.is_empty() is False

    def test_pop_front(self):
        d = Deque(['A', 'B', 'C'])
        assert d.pop_front() == 'A'
        assert d.length() == 2
        assert d.pop_front() == 'B'
        assert d.length() == 1
        assert d.pop_front() == 'C'
        assert d.length() == 0
        assert d.is_empty() is True
        with self.assertRaises(ValueError):
            d.pop_front()

    def test_pop_back(self):
        d = Deque(['A', 'B', 'C'])
        assert d.pop_back() == 'C'
        assert d.length() == 2
        assert d.pop_back() == 'B'
        assert d.length() == 1
        assert d.pop_back() == 'A'
        assert d.length() == 0
        print(d.list.size)
        assert d.is_empty() is True
        with self.assertRaises(ValueError):
            d.pop_back()

if __name__ == '__main__':
    unittest.main()