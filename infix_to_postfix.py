"""
Tomas McNamer
infix_to_postfix.py

This module house the infix_to_postfix function, which converts an infix
expression to postfix notation.
"""
from adt import Stack, Queue
from operators import Operators, ops
from eval_postfix import eval_postfix


# A dictionary containing the precedence of each operator
# Greater values indicate higher precedence, this follows
# PEMDAS, note the parentheses have the lowest precedence
# because we already handle them separately
operator_precedence = {
    Operators.ADD: 1,
    Operators.SUB: 1,
    Operators.MUL: 5,
    Operators.DIV: 5,
    Operators.EXP: 10,
    Operators.RPAREN: 0,
    Operators.LPAREN: 0,
}


def infix_to_postfix(string: str) -> Queue:
    """Takes an infix expression and converts it to postfix notation.

    Args:
        string (str): The infix expression to convert.

    Returns:
        Queue: The corresponding postfix expression.
    """
    output = Queue()
    operator_stack = Stack()

    i = -1
    buffer = ""

    # Wrap the expression in parentheses to make parsing easier
    # This would denote the start and end of the expression``
    string += ")"
    operator_stack.push(Operators.LPAREN)

    # Whether or not the last character was an operator
    # This is useful for parsing negative numbers, as we would be
    # able to tell whether a number is expected (ie. a '-' is to be
    # interpreted as a negative sign) or not (ie. a '-' is a subtraction
    # operator)
    last_char_was_op = True

    while i + 1 < len(string): # Iterate through the string
        i += 1
        char = string[i]

        # If the character is an operator, and we are expecting one
        # (ie. the last character was not an operator). Note the exception
        # for the opening parenthesis, which can be seen after an operator
        # eg. '2*(3+4)'
        if char in ops and (not last_char_was_op or char == "("):
            last_char_was_op = True
            operator = ops[char]

            # Mark the beginning of a parenthesized group
            # Used later when encountering the matching closing
            # parenthesis
            if operator == Operators.LPAREN:
                operator_stack.push(operator)

            # If the operator is a closing parenthesis, pop all operators
            # into the output until the matching opening parenthesis is found
            elif operator == Operators.RPAREN:
                last_char_was_op = False # Parentheses are not operators
                while operator_stack.top() != Operators.LPAREN:
                    output.push(operator_stack.pop())
                operator_stack.pop()  # Remove the opening parenthesis from the stack

            # Pop all operators with greater precendence from the stack into the output
            # before pushing the current operator onto the stack
            else:
                while operator_precedence[operator] <= operator_precedence[operator_stack.top()]:
                    output.push(operator_stack.pop())
                operator_stack.push(operator)

        # We are expecting a number or variable, the can go directly into the output
        else:
            last_char_was_op = False
            buffer = char

            # If the first character is a negative sign or a number, we have
            # a number literal to parse
            if char.isnumeric() or char == "-":

                # While the next character is a number or a decimal point, append
                # it to the buffer. Note that we obviously only allow one decimal point per
                # number
                while (i + 1 < len(string)) and (
                    (string[i + 1]).isnumeric()
                    or (string[i + 1] == "." and buffer.count(".") == 0)
                ):
                    i += 1
                    buffer += string[i]
                output.push(float(buffer))

            # We assume the following token is a variable name, so parse it
            else:
                # While the next character is alphanumeric, append it to the buffer (note that
                # this allows for variable names to contain numbers, but not start with them)
                while i + 1 < len(string) and (
                    string[i+1].isalnum()
                ):
                    i += 1
                    buffer += string[i]

                # Push the variable name as is into the output
                output.push(buffer)
            continue

    # Finally pop all remaining operators into the output
    while not operator_stack.is_empty() and not operator_stack.top() == Operators.LPAREN:
        output.push(operator_stack.pop())

    return output


if __name__ == "__main__":
    out = infix_to_postfix("res1+2")
    print(out)
    r = eval_postfix(out, {'res1': 2})
    print(r)
