from adt import Stack, Queue
from operators import Operators, ops
from eval_postfix import eval_postfix

operator_precedence = {
    Operators.ADD: 1,
    Operators.SUB: 1,
    Operators.MUL: 5,
    Operators.DIV: 5,
    Operators.EXP: 10,
    Operators.RPAREN: 0,
    Operators.LPAREN: 0,
}


def infix_to_postfix(string: str):
    output = Queue()
    op_stack = Stack()

    i = -1
    buffer = ""
    string += ")"
    op_stack.push(Operators.LPAREN)
    last_char_was_op = True
    while i + 1 < len(string):
        i += 1
        char = string[i]
        if char in ops and (not last_char_was_op or char == "("):
            last_char_was_op = True
            op = ops[char]
            if op == Operators.LPAREN:
                op_stack.push(op)
            elif op == Operators.RPAREN:
                last_char_was_op = False
                while op_stack.top() != Operators.LPAREN:
                    output.push(op_stack.pop())
                op_stack.pop()  # Remove LPAREN
            else:
                while operator_precedence[op] <= operator_precedence[op_stack.top()]:
                    output.push(op_stack.pop())
                op_stack.push(op)
        else:
            last_char_was_op = False
            buffer = char
            if char.isnumeric() or char == "-":
                while (i + 1 < len(string)) and (
                    (string[i + 1]).isnumeric()
                    or (string[i + 1] == "." and buffer.count(".") == 0)
                ):
                    i += 1
                    buffer += string[i]
            else:
                # TODO: Parse variables 
                pass
            output.push(float(buffer))
            continue

    while not op_stack.is_empty():
        output.push(op_stack.pop())

    print("foutput", output)
    return output


if __name__ == "__main__":
    out = infix_to_postfix("-2-9")
    r = eval_postfix(out)
    print(r)
