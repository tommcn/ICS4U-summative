"""
Tomas McNamer
eval_postfix.py

This modules contains the function eval_postfix, which takes a postfix expression
and evaluates it.
"""
from math import factorial

from McNamer_Tomas_adt import Stack, Queue
from McNamer_Tomas_helpers import VariableNotFound, VariablesType
from McNamer_Tomas_operators import Operators, SINGLE_OPERAND_OPERATORS


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
    working_stack = Stack()  # The stack that houses the intermediate results

    # Walrus operator, this is a while loop that also assigns the top of the stack to
    # the variable top, and runs until the stack is empty (ie. falsy)
    while (top := postfix.pop()) is not None:
        # If the top of the stack is an operator, then we can do maths with it
        if isinstance(top, Operators):
            # We need to pop the operands in reverse order as they are in a stack
            rhs = working_stack.pop()
            # If either of the operands are variables, we need to look them up in the
            # variables dictionary
            if isinstance(rhs, str):
                try:
                    rhs = variables[rhs]
                except KeyError as err:
                    raise VariableNotFound(f"The variable {rhs} is undefined") from err

            # If the operator requires two operands
            if top not in SINGLE_OPERAND_OPERATORS:
                lhs = working_stack.pop()
                if isinstance(lhs, str):
                    try:
                        lhs = variables[lhs]
                    except KeyError as err:
                        raise VariableNotFound(
                            f"The variable {lhs} is undefined"
                        ) from err

            # Match the operator and do the corresponding operation
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
                    working_stack.push(lhs**rhs)
                case Operators.FCT:
                    working_stack.push(factorial(int(rhs)))

                case _:  # Should be unreachable, but just in case something goes wrong
                    raise NotImplementedError
        else:
            if isinstance(top, str):
                try:
                    top = variables[top]
                except KeyError as err:
                    raise VariableNotFound(f"The variable {top} is undefined") from err
            working_stack.push(top)

    # The result is the last thing left in the stack
    return working_stack.pop()


# Example program
if __name__ == "__main__":
    equation = Stack.from_list(
        [2, 3, 1, Operators.MUL, Operators.ADD, 9, Operators.SUB]
    )
    res = eval_postfix(equation, {})
    print(res)
