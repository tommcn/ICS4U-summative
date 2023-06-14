###############################################################################
# NAME: Tomas McNamer
# COURSE: ICS4U
# FILE: McNamer_Tomas_operators.py
# DESCRIPTION: Houses the variables needed for operators to function
###############################################################################
from enum import Enum


# How to add a new operator:
# 1. Add the operator short name to the enum below
# 2. Add the operator symbol (as ONE character) to the dictionnary
# 3. If it only requires a single operand (eg. square root), add it to the list
# 4. Add its precedence to the precedence dictionnary (higher number -> higher precedence)
# 5. Implement the operation in the switch case of the eval_postfix file


class Operators(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    EXP = "^"
    FCT = "!"
    LPAREN = "("
    RPAREN = ")"


ops = {
    "+": Operators.ADD,
    "-": Operators.SUB,
    "*": Operators.MUL,
    "/": Operators.DIV,
    "^": Operators.EXP,
    "!": Operators.FCT,
    "(": Operators.LPAREN,
    ")": Operators.RPAREN,
}

SINGLE_OPERAND_OPERATORS = [
    Operators.FCT,
]

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
    Operators.FCT: 15,
    Operators.RPAREN: 0,
    Operators.LPAREN: 0,
}
