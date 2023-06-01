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


def isnumeric(c):
    return c.isnumeric() or c == "." or c == "-"


def infix_to_postfix(string):
    output = Queue()
    op_stack = Stack()

    i = -1
    buffer = ""
    string += ")"
    op_stack.push(Operators.LPAREN)
    while i + 1 < len(string):
        i += 1
        print()
        print("Output Stack:", output)
        print("Operator Stack", op_stack)
        char = string[i]
        # Rewrite to while loop lol
        if isnumeric(char):
            print("1")
            buffer = char
            while i + 1 < len(string) and isnumeric(string[i+1]):
                i+=1
                buffer += string[i]
            output.push(float(buffer))
            continue
        if char in ops:
            op = ops[char]
            if op == Operators.LPAREN:
                print("2")
                op_stack.push(op)
            elif op == Operators.RPAREN:
                print("3")
                while op_stack.top() != Operators.LPAREN:
                    output.push(op_stack.pop())
                op_stack.pop() # Remove LPAREN
            else:
                print("5")
                while operator_precedence[op] <= operator_precedence[op_stack.top()]:
                    output.push(op_stack.pop())
                op_stack.push(op)
            continue

    while not op_stack.is_empty():
        output.push(op_stack.pop())

    print("foutput", output)
    return output


if __name__ == "__main__":
    out = infix_to_postfix("(1+2)*3")
    r = eval_postfix(out)
    print(r)
