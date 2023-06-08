from enum import Enum


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
