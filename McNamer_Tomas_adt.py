###############################################################################
# NAME: Tomas McNamer
# COURSE: ICS4U
# FILE: McNamer_Tomas_adt.py
# DESCRIPTION: Houses the Abstract Data Classes (ADT) which are used to store
#                   These are essentially utility classes.
###############################################################################


###############################################################################
# CLS NAME: Stack
# DESCRIPTION: Implements a simple stack using python's builtins lists (FILO)
###############################################################################
class Stack:
    def __init__(self):
        self.__data = []

    def is_empty(self):
        return len(self.__data) == 0

    @classmethod
    def from_list(cls, data):
        new = cls()
        # Reverse the list since we are popping from the end
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

###############################################################################
# CLS NAME: Queue
# DESCRIPTION: Implements a simple queue using python's builtins lists (FIFO)
###############################################################################
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
