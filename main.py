from eval_postfix import eval_postfix
from operators import Operators
from adt import Stack



def create_postfix_equation():
    s = Stack.from_list([2, 3, 1, Operators.MUL, Operators.ADD, 9, Operators.SUB])
    return s


def main():
    eq = create_postfix_equation()
    r = eval_postfix(eq)
    print(r)


if __name__ == "__main__":
    main()
