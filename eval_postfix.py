from stack import Stack
from operators import Operators

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
                case Operators.DIV:
                    working_stack.push(lhs / rhs)
                case Operators.EXP:
                    working_stack.push(lhs ** rhs)
        else:
            working_stack.push(top)
    return working_stack.pop()

def main():
    eq = Stack.from_list([2, 3, 1, Operators.MUL, Operators.ADD, 9, Operators.SUB])
    r = eval_postfix(eq)
    print(r)


if __name__ == "__main__":
    main()
