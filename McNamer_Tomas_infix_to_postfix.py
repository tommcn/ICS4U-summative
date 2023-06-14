###############################################################################
# NAME: Tomas McNamer
# COURSE: ICS4U
# FILE: McNamer_Tomas_infix_to_postfix.py
# DESCRIPTION: Houses the infix_to_postfix function, which converts an infix
#                   expression to postfix notation.
###############################################################################
from string import ascii_letters

from McNamer_Tomas_adt import Stack, Queue
from McNamer_Tomas_helpers import ImproperExpression
from McNamer_Tomas_operators import Operators, ops, SINGLE_OPERAND_OPERATORS, operator_precedence
from McNamer_Tomas_eval_postfix import eval_postfix


###############################################################################
# FCN NAME: infix_to_postfix
# DESCRIPTION: Convert and infix expression to a postfix one
# INPUTS: string - str - The input string
# OUTPUTS: Queue - A queue containing the postfix expression
# ALGORITHM:
#   SET output TO NEW Queue
#   SET operator stack TO NEW stack
#   SET i TO -1
#   SET buffer TO EMPTY STRING
#   ADD ) TO string
#   PUSH TO operator stack VALUE (
#   SET expecting number TO TRUE
#
#   WHILE i SMALLER THEN length of string
#       IF operator encountered
#           SET expecting number TO true
#           IF operator IS (
#               PUSH TO operator stack VALUE (
#           ELSEIF operator IS )
#               UNTIL a ( IS reached DO
#                   PUSH TO ouput VALUE (CALL pop ON operator stack)
#               ENDUNTIL
#               CALL pop ON operator stack
#           ELSE
#               UNTIL an operator with smaller precedence is reached DO
#                   PUSH TO output VALUE (CALL pop ON operator stack)
#               ENDUNTIL
#               PUSH TO operator stack VALUE operator
#               IF operator only required one operand
#                   SET expecting number TO false
#               ENDIF
#           ELSE
#               SET expecting number TO false
#               SET buffer TO character
#               UNTIL end of number or variable is reached DO
#                   ADD TO buffer next character
#               ENDUNTIL
#               IF buffer IS a number
#                   PARSE buffer AS float INTO buffer
#               ENDIF
#               PUSH TO output VALUE buffer
#           ENDIF
#   ENDWHILE
#   WHILE operator stack is not empty
#       PUSH TO output VALUE (CALL pop ON operator stack)
#   ENDWHILE
#   RETURN output
###############################################################################
def infix_to_postfix(string: str) -> Queue:
    output = Queue()
    operator_stack = Stack()

    i = -1
    buffer = ""

    # Wrap the expression in parentheses to make parsing easier
    # This would denote the start and end of the expression``
    string += ")"
    operator_stack.push(Operators.LPAREN)

    # Whether or not we are expecting a number
    # This is useful for parsing negative numbers, as we would be
    # able to tell whether a number is expected (ie. a '-' is to be
    # interpreted as a negative sign) or not (ie. a '-' is a subtraction
    # operator)
    expecting_number = True

    while i + 1 < len(string):  # Iterate through the string
        i += 1
        char = string[i]

        # If the character is an operator, and we are expecting one
        # (ie. the last character was not an operator). Note the exception
        # for the opening parenthesis, which can be seen after an operator
        # eg. '2*(3+4)'
        if char in ops and (not expecting_number or char == "("):
            expecting_number = True
            operator = ops[char]

            # Mark the beginning of a parenthesized group
            # Used later when encountering the matching closing
            # parenthesis
            if operator == Operators.LPAREN:
                operator_stack.push(operator)

            # If the operator is a closing parenthesis, pop all operators
            # into the output until the matching opening parenthesis is found
            elif operator == Operators.RPAREN:
                expecting_number = False  # Parentheses are not operators
                while operator_stack.top() != Operators.LPAREN:
                    output.push(operator_stack.pop())
                operator_stack.pop()  # Remove the opening parenthesis from the stack

            # Pop all operators with greater precendence from the stack into the output
            # before pushing the current operator onto the stack
            else:
                while (
                    operator_precedence[operator]
                    <= operator_precedence[operator_stack.top()]
                ):
                    output.push(operator_stack.pop())
                operator_stack.push(operator)

            # If the operator only expects one operand (eg. factorial), then the
            # next token will be another operator (eg. 5! + 2)
            if operator in SINGLE_OPERAND_OPERATORS:
                expecting_number = False

        # We are expecting a number or variable, the can go directly into the output
        else:
            expecting_number = False
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
            elif char in ascii_letters:
                # While the next character is alphanumeric, append it to the buffer (note that
                # this allows for variable names to contain numbers, but not start with them)
                while i + 1 < len(string) and (string[i + 1].isalnum()):
                    i += 1
                    buffer += string[i]

                # Push the variable name as is into the output
                output.push(buffer)
            else:
                raise ImproperExpression(
                    f"The expression {string} is not a valid one (hint: look at character {i})"
                )
            continue

    # Finally pop all remaining operators into the output
    while (
        not operator_stack.is_empty() and not operator_stack.top() == Operators.LPAREN
    ):
        output.push(operator_stack.pop())

    return output

# Some example code
if __name__ == "__main__":
    out = infix_to_postfix("res1+2")
    print(out)
    r = eval_postfix(out, {"res1": 2})
    print(r)
