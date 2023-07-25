from collections import deque

class CircularQueue:
    def __init__(self, max_size):
        self.__data = deque(max_size)
        self.__max_size = max_size

    def append(self, item):
        self.__data.append(item)

    def first(self):
        return self.__data[0]

    def last(self):
        return self.__data[self.__max_size - 1]
