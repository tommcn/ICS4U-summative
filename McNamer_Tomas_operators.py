from enum import Enum


class Operators(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    EXP = "^"
    LPAREN = "("
    RPAREN = ")"


ops = {
    "+": Operators.ADD,
    "-": Operators.SUB,
    "*": Operators.MUL,
    "/": Operators.DIV,
    "^": Operators.EXP,
    "(": Operators.LPAREN,
    ")": Operators.RPAREN
}
