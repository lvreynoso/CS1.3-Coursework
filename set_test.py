#!python

from set import Set
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init(self):
        st = Set([6, 9, 4, 2, 0, 'X', 'MJ', 'Santa Cruz'])
        assert st.size == 8
        assert len(st) == 8

if __name__ == '__main__':
    unittest.main()