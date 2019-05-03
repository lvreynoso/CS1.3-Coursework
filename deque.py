#!python

from linkedlist import LinkedList


class Deque(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push_back(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this queue."""
        return self.list.length()

    def push_back(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1), LL has a reference to the tail
        and the item is appended after that"""
        self.list.append(item)

    def push_front(self, item):
        """Insert the given item at the front of this queue.
        Running time: O(1), LL has a reference to the head
        and the item is prepended before that"""
        self.list.prepend(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.list.head.data

    def back(self):
        """Return the item at the back of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.list.tail.data

    def pop_back(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(n) because we have to delete the tail in 
        a singly linked list :("""
        if self.is_empty():
            raise ValueError('Attempt to pop empty queue')
        data = self.list.tail.data
        # delete the tail. a doubly linked list would be better...
        # this is really hack lmao
        previous = None
        current = self.list.head
        for _ in range(self.list.length() - 1):
            previous = current
            current = current.next
        if previous is None:
            self.list.head = None
        else:
            previous.next = None
        self.list.tail = previous
        self.list.size -= 1
        return data

    def pop_front(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) because we always dequeue the head"""
        data = self.list[0]
        self.list.delete(data)
        return data