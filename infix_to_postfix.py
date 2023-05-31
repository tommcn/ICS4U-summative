from stack import Stack, Queue
from operators import Operators, ops
from eval_postfix import eval_postfix

operator_precedence = {
    Operators.ADD: 1,
    Operators.SUB: 1,
    Operators.MUL: 5,
    Operators.DIV: 5,
    Operators.EXP: 10,
    Operators.RPAREN: -1,
    Operators.LPAREN: 15,
}


def isnumeric(c):
    return c.isnumeric() or c == "." or c == "-"


def infix_to_postfix(string):
    output = Queue()
    op_stack = Stack()

    i = -1
    buffer = ""
    while i + 1 < len(string):
        i += 1
        print("Output Stack:", output)
        print("Operator Stack", op_stack)
        char = string[i]
        print(i)
        # Rewrite to while loop lol
        if isnumeric(char):
            buffer = char
            while i + 1 < len(string) and isnumeric(string[i+1]):
                i+=1
                buffer += string[1]
            output.push(float(buffer))
            continue
        if char in ops:
            op = ops[char]
            if op_stack.is_empty():
                op_stack.push(op)
            elif op == Operators.LPAREN:
                op_stack.push(op)
            elif op == Operators.RPAREN:
                while op_stack.top() != Operators.LPAREN:
                    output.push(op_stack.pop())
                op_stack.pop()
            elif operator_precedence[op] > operator_precedence[op_stack.top()]:
                op_stack.push(op)
            elif operator_precedence[op] < operator_precedence[op_stack.top()]:
                while (not op_stack.is_empty() and 
                        operator_precedence[op] > operator_precedence[op_stack.top()]):
                    output.push(op_stack.pop())
                op_stack.push(op)
            else:
                op_stack.push(op)
            continue

    while not op_stack.is_empty():
        output.push(op_stack.pop())

    print("foutput", output)
    return output


if __name__ == "__main__":
    out = infix_to_postfix("2+9*2/2")
    r = eval_postfix(out)
    print(r)