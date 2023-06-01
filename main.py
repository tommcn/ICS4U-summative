from eval_postfix import eval_postfix
from infix_to_postfix import infix_to_postfix
from operators import Operators
from adt import Stack

IFNAME = "McNamer_Tomas_input.txt"
OFNAME = "McNamer_Tomas_output.txt"

def create_postfix_equation():
    s = Stack.from_list([2, 3, 1, Operators.MUL, Operators.ADD, 9, Operators.SUB])
    return s

def main():
    results = []
    with open(IFNAME, "r", encoding="UTF-8") as f:
        for line in f.readlines():
            postfix = infix_to_postfix(line)
            result = eval_postfix(postfix)
            results.append(str(result) + "\n")

    with open(OFNAME, "w", encoding="UTF-8") as f:
        f.writelines(results)



if __name__ == "__main__":
    main()
