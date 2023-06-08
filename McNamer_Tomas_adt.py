class Stack:
    def __init__(self):
        self.__data = []

    def is_empty(self):
        return len(self.__data) == 0

    @classmethod
    def from_list(cls, data):
        new = cls()
        new._set_stack(data[::-1])
        return new

    def _set_stack(self, data):
        self.__data = data

    def push(self, datum):
        self.__data.append(datum)
        return True

    def top(self):
        return self.__data[-1]

    def pop(self):
        if len(self.__data) == 0:
            return None

        return self.__data.pop(-1)

    def __str__(self):
        return str(self.__data)


class Queue:
    def __init__(self):
        self.__data = []

    def is_empty(self):
        return len(self.__data) == 0

    def _set_queue(self, data):
        self.__data = data

    def push(self, datum):
        self.__data.append(datum)
        return True

    def peek(self):
        return self.__data[0]

    def pop(self):
        if len(self.__data) == 0:
            return None

        return self.__data.pop(0)

    def get_data(self):
        return self.__data

    def __str__(self):
        return str(self.__data)
