###############################################################################
# NAME: Tomas McNamer
# COURSE: ICS4U
# FILE: McNamer_Tomas_eval_postfix.py
# DESCRIPTION: Houses the function responsible for the evaluating postfix
#              expressions.
###############################################################################
from math import factorial

from McNamer_Tomas_adt import Stack, Queue
from McNamer_Tomas_helpers import VariableNotFound, VariablesType
from McNamer_Tomas_operators import Operators, SINGLE_OPERAND_OPERATORS

###############################################################################
# FCN NAME: eval_postfix
# DESCRIPTION: Evaluates an expression in postfix form
# INPUTS: postfix - Queue - The postfix expression to evaluate
#         variables - VariablesType - The variables to use when evaluating the
#               expression
# OUTPUTS: float - The result of the expression
# RAISES: NotImplementedError - Technically unreachable, throws when
#               encountering an unknown operator
# ALGORITHM:
#   SET working_stack TO NEW stack
#   WHILE postfix NOT EMPTY
#       IF postfix's top IS an operator
#           IF operator REQUIRES two operands
#               POP rhs and lhs FROM working stack
#           ELSE
#               POP rhs FROM working stack
#           ENDIF
#           IF EITHER operands ARE string
#               UPDATE them to the value from variables dict
#           ENDIF
#           EVALUATE the operator with rhs (and possibly lhs) INTO result
#           PUSH TO working stack VALUE result
#       ELSE
#           PUSH TO working stack VALUE postfix's top
#       ENDIF
#   ENDWHILE
#   RETURN TOP OF working_stack
###############################################################################
def eval_postfix(postfix: Queue, variables: VariablesType) -> float:
    working_stack = Stack()  # The stack that houses the intermediate results

    # Walrus operator, this is a while loop that also assigns the top of the stack to
    # the variable top, and runs until the stack is empty (ie. falsy)
    while (top := postfix.pop()) is not None:
        # If the top of the stack is an operator, then we can do maths with it
        if isinstance(top, Operators):
            # We need to pop the operands in reverse order as they are in a stack
            rhs = working_stack.pop()

            # If the operator requires two operands
            if top not in SINGLE_OPERAND_OPERATORS:
                lhs = working_stack.pop()

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
            # If top is a string, push its numerical representation, this serves to simplifies
            # the math logic above
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
