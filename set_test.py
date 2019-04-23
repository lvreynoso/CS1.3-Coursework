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

    def test_add_and_contains(self):
        st = Set()
        assert st.size == 0
        st.add(6)
        st.add(4)
        st.add('MJ')
        assert st.size == 3
        assert st.contains(6) is True
        assert st.contains(4) is True
        assert st.contains('MJ') is True
        assert st.contains('X') is False
        assert st.contains(9) is False

    def test_remove(self):
        st = Set()
        assert st.size == 0
        st.add(6)
        st.add(4)
        st.add('MJ')
        assert st.size == 3
        assert st.contains(6) is True
        assert st.contains(4) is True
        assert st.contains('MJ') is True
        st.remove(6)
        st.remove('MJ')
        assert st.size == 1
        assert st.contains(6) is False
        assert st.contains('MJ') is False
        assert st.contains(4) is True
        with self.assertRaises(KeyError):
            st.remove('X')
        with self.assertRaises(KeyError):
            st.remove(6)

    def test_union(self):
        st = Set([6, 9, 4, 2, 0, 'X', 'MJ', 'Santa Cruz'])
        other = Set([6, 4, 18, 21, 'X', 'Nintendo', 'Sony'])
        union_set = st.union(other)
        assert union_set.contains(6) is True
        assert union_set.contains(9) is True
        assert union_set.contains(4) is True
        assert union_set.contains(2) is True
        assert union_set.contains(0) is True
        assert union_set.contains(18) is True
        assert union_set.contains(21) is True
        assert union_set.contains('X') is True
        assert union_set.contains('MJ') is True
        assert union_set.contains('Santa Cruz') is True
        assert union_set.contains('Nintendo') is True
        assert union_set.contains('Sony') is True
        assert union_set.size == 12

    def test_intersection(self):
        st = Set([6, 9, 4, 2, 0, 'X', 'MJ', 'Santa Cruz'])
        other = Set([6, 4, 18, 21, 'X', 'Nintendo', 'Sony'])
        intersection_set = st.intersection(other)
        assert intersection_set.contains(6) is True
        assert intersection_set.contains(4) is True
        assert intersection_set.contains('X') is True
        assert intersection_set.contains(18) is False
        assert intersection_set.contains('Santa Cruz') is False
        assert intersection_set.size == 3

    def test_difference(self):
        st = Set([6, 9, 4, 2, 0, 'X', 'MJ', 'Santa Cruz'])
        other = Set([6, 4, 18, 21, 'X', 'Nintendo', 'Sony'])
        difference_set = st.difference(other)
        assert difference_set.contains(9) is True
        assert difference_set.contains(2) is True
        assert difference_set.contains(0) is True
        assert difference_set.contains('MJ') is True
        assert difference_set.contains('Santa Cruz') is True
        assert difference_set.contains(6) is False
        assert difference_set.contains(4) is False
        assert difference_set.contains('X') is False
        assert difference_set.size == 5

    def test_is_subset(self):
        st = Set([6, 9, 4, 2, 0, 'X', 'MJ', 'Santa Cruz'])
        other = Set([6, 4, 18, 21, 'X', 'Nintendo', 'Sony'])
        sub = Set([4, 2, 0, 'MJ'])
        assert st.is_subset(other) is False
        assert st.is_subset(sub) is True
        assert st.is_subset(st) is True

if __name__ == '__main__':
    unittest.main()