#!python

from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        # Initialize the set with the given elements
        if elements is not None:
            self.orb = HashTable(len(elements) * 2)
            for element in elements:
                self.orb.set(element, None)
        else:
            self.orb = HashTable()
        self.size = self.orb.size

    def __str__(self):
        items = ['{!r}'.format(element) for element in self]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        return 'Set({!r})'.format(self.orb.keys())

    def __contains__(self, item):
        return self.contains(item)

    def __len__(self):
        return self.size

    def __iter__(self):
        return self._generator()

    def _generator(self):
        elements = self.orb.keys()
        for element in elements:
            yield element

    def contains(self, element):
        return self.orb.contains(element)

    def add(self, element):
        self.orb.set(element, None)
        self.size = self.orb.size

    def remove(self, element):
        self.orb.delete(element)
        self.size = self.orb.size

    def union(self, other_set):
        union_set = Set(self)
        for element in other_set:
            union_set.add(element)
        return union_set

    def intersection(self, other_set):
        inter_set = Set()
        if len(other_set) < len(self):
            for element in other_set:
                if element in self:
                    inter_set.add(element)
        else:
            for element in self:
                if element in other_set:
                    inter_set.add(element)
        return inter_set

    def difference(self, other_set):
        diff_set = Set(self)
        if len(other_set) < len(self):
            for element in other_set:
                if element in self:
                    diff_set.remove(element)
        else:
            for element in self:
                if element in other_set:
                    diff_set.remove(element)
        return diff_set

    def is_subset(self, other_set):
        for element in other_set:
            if element not in self:
                return False
        return True

    def symmetric_difference(self, other_set):
        symmetric_set = Set(self)
        for element in other_set:
            if element in symmetric_set:
                symmetric_set.remove(element)
            else:
                symmetric_set.add(element)
        return symmetric_set


def test_set():
    test = Set()
    print('Set: ' + str(test))

    print('Setting entries:')
    test.add('S')
    print('set(S): ' + str(test))
    test.add('A')
    print('set(A): ' + str(test))
    test.add('F')
    print('set(F): ' + str(test))
    test.add('E')
    print('set(E): ' + str(test))
    # print('Set: ' + str(test))
    print('size: ' + str(test.size) + '\n')

    print('Checking entries:')
    print('contains(S): ' + str(test.contains('S')))
    print('contains(A): ' + str(test.contains('A')))
    print('contains(F): ' + str(test.contains('F')))
    print('contains(E): ' + str(test.contains('E')))
    print('')

    print('Removing entries:')
    test.remove('S')
    print('remove(S): ' + str(test))
    test.remove('A')
    print('remove(A): ' + str(test))
    test.remove('F')
    print('remove(F): ' + str(test))
    test.remove('E')
    print('remove(E): ' + str(test))
    print('contains(F): ' + str(test.contains('F')))
    print('size: ' + str(test.size))

if __name__ == '__main__':
    test_set()