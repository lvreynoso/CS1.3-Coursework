#!python

class CircularBuffer(object):
    """docstring for CircularBuffer"""
    def __init__(self, max_size):
        data = [None] * max_size
        self.max_size = max_size
        self.size = 0

        # two pointers that keep track of where we are
        # writing to and reading from
        self.write_index = 0
        self.read_index = 0

    def is_empty():
        return self.size == 0

    def is_full():
        return self.size == self.max_size

    def enqueue(item):
        self.data[write_index] = item
        self.write_index += 1
        if self.write_index == len(data):
            self.write_index = 0
        self.size += 1

    def front():
        return self.data[self.read_index]

    def dequeue():
        front_item = self.front()
        self.data[self.read_index] = None
        self.read_index += 1
        if self.read_index == len(data):
            self.read_index = 0
        self.size -= 1
        return front_item

