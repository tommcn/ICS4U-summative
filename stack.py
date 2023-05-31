class Stack(object):
    __data = []

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
            return False

        return self.__data.pop(-1)

    def __str__(self):
        return str(self.__data)
