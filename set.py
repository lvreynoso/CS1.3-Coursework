#!python

from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        # Initialize the set with the given elements
        if elements is not None:
            self.orb = HashTable(len(elements))
            for element in elements:
                self.orb.set(element, None)
        else:
            self.orb = HashTable()
        self.size = self.orb.size

    def __contains__(self, item):
        return self.contains(item)

    def __len__(self):
        return self.size

    def __iter__(self):
        return self._generator()

    def _generator():
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