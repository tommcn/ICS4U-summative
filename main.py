from enum import Enum


class Operators(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    EXP = "^"


ops = {
    "+": Operators.ADD,
    "-": Operators.SUB,
    "*": Operators.MUL,
    "/": Operators.DIV,
    "^": Operators.EXP,
}


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
        else:
            return self.__data.pop(-1)

    def __str__(self):
        return str(self.__data)


def create_postfix_equation():
    s = Stack.from_list([2, 3, 1, Operators.MUL, Operators.ADD, 9, Operators.SUB])
    return s


def eval_postfix(p):
    working_stack = Stack()
    while top := p.pop():
        if isinstance(top, Operators):
            rhs = working_stack.pop()
            lhs = working_stack.pop()
            match top:
                case Operators.ADD:
                    working_stack.push(lhs + rhs)
                case Operators.MUL:
                    working_stack.push(lhs * rhs)
                case Operators.SUB:
                    working_stack.push(lhs - rhs)
        else:
            working_stack.push(top)
        print(working_stack)

    return working_stack.pop()

def main():
    eq = create_postfix_equation()
    r = eval_postfix(eq)
    print(r)


if __name__ == "__main__":
    main()
