from adt import Stack, Queue
from helpers import VariablesType
from operators import Operators

def eval_postfix(postfix: Queue, variables: VariablesType) -> float:
    """Evaluates an expression in postfix form

    Args:
        postfix (Queue): The postfix expression to evalute
        variables (VariablesType): A dictionary of variables to be used when encoutering a variable

    Raises:
        NotImplementedError: Technically unreachable, throws when encountering an unknown operator

    Returns:
        float: The result of the expression (beware of floating point arithmetic inacuracy)
    """
    working_stack = Stack()
    while top := postfix.pop():
        if isinstance(top, Operators):
            rhs = working_stack.pop()
            lhs = working_stack.pop()

            if isinstance(rhs, str):
                rhs = variables[rhs]
            if isinstance(lhs, str):
                lhs = variables[lhs]

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
                case _:
                    raise NotImplementedError
        else:
            working_stack.push(top)
    return working_stack.pop()

def main():
    """Example program
    """
    equation = Stack.from_list([2, 3, 1, Operators.MUL, Operators.ADD, 9, Operators.SUB])
    res = eval_postfix(equation, {})
    print(res)


if __name__ == "__main__":
    main()
