#!python

class CircularBuffer(object):
    """docstring for CircularBuffer"""
    def __init__(self, max_size=8):
        self.data = [None] * max_size
        self.max_size = max_size
        self.size = 0

        # two pointers that keep track of where we are
        # writing to and reading from
        self.write_index = 0
        self.read_index = 0

    def __str__(self):
        items = []
        for index, value in enumerate(self.data):
            if index == self.write_index and index == self.read_index:
                items.append('*&{!r}'.format(value))
            elif index == self.write_index:
                items.append('&{!r}'.format(value))
            elif index == self.read_index:
                items.append('*{!r}'.format(value))
            else:
                items.append('{!r}'.format(value))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        items = []
        temp_index = self.read_index
        for count in range(len(self.data)):
            items.append(self.data[temp_index])
            temp_index = (temp_index + 1) % self.max_size
        return 'CircularBuffer({!r})'.format(items)

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def enqueue(self, item):
        if self.data[self.write_index] is not None:
            self.read_index = (self.read_index + 1) % self.max_size
        else:
            self.size += 1
        self.data[self.write_index] = item
        self.write_index = (self.write_index + 1) % self.max_size

    def front(self):
        return self.data[self.read_index]

    def dequeue(self):
        if self.is_empty():
            return None
        front_item = self.front()
        self.data[self.read_index] = None
        self.read_index = (self.read_index + 1) % self.max_size
        self.size -= 1
        return front_item

def test_circular_buffer():
    cb = CircularBuffer(4)
    print('Circular Buffer: ' + str(cb))
    cb.enqueue('Alpha')
    print('Circular Buffer: ' + str(cb))
    cb.enqueue('Beta')
    print('Circular Buffer: ' + str(cb))
    cb.enqueue('Gamma')
    print('Circular Buffer: ' + str(cb))
    cb.enqueue('Delta')
    print('Circular Buffer: ' + str(cb))

    cb.enqueue('Epsilon')
    print('Circular Buffer: ' + str(cb))

    print(cb.front())
    cb.dequeue()
    print('Circular Buffer: ' + str(cb))
    print(cb.front())
    cb.dequeue()
    print('Circular Buffer: ' + str(cb))
    print(cb.front())
    cb.dequeue()
    print('Circular Buffer: ' + str(cb))
    print(cb.front())
    cb.dequeue()
    print('Circular Buffer: ' + str(cb))
    print(cb.front())
    cb.dequeue()
    print('Circular Buffer: ' + str(cb))


if __name__ == '__main__':
    test_circular_buffer()