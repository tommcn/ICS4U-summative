"""
Tomas McNamer
"""
from string import ascii_letters

from eval_postfix import eval_postfix
from helpers import VariablesType
from infix_to_postfix import infix_to_postfix

ACCEPTABLE_VARIABLE_CHARACTERS = ascii_letters + "_"

IFNAME = "McNamer_Tomas_input.txt"
OFNAME = "McNamer_Tomas_output.txt"


def pipeline(expr: str, variables: VariablesType) -> tuple[str | float, VariablesType]:
    varname = None
    if "=" in expr:
        varname, expr = expr.split("=")
    postfix = infix_to_postfix(expr)
    result = eval_postfix(postfix, variables)
    if varname is not None:
        variables[varname] = result
        result = varname + "=" + str(result)

    return result, variables


def main():
    results = []
    variables = {
        "PI": 3.14159,
        "e": 2.71828
    }
    with open(IFNAME, "r", encoding="UTF-8") as f:
        for line in f.readlines():
            result, variables = pipeline(line.rstrip(), variables)
            results.append(str(result) + "\n")

    with open(OFNAME, "w", encoding="UTF-8") as f:
        f.writelines(results)



if __name__ == "__main__":
    main()
