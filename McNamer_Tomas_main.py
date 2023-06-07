"""
Tomas McNamer
"""

from McNamer_Tomas_eval_postfix import eval_postfix
from McNamer_Tomas_helpers import VariablesType
from McNamer_Tomas_infix_to_postfix import infix_to_postfix


IFNAME = "McNamer_Tomas_input.txt"
OFNAME = "McNamer_Tomas_output.txt"


def pipeline(expr: str, variables: VariablesType) -> tuple[str | float, VariablesType]:
    """Runs the whole program from an original string to a numerical result

    Args:
        expr (str): The expression, as a string in infix form
        variables (VariablesType): The variables to be used during evaluation

    Returns:
        tuple[str | float, VariablesType]: Two variables, 1: the result as a float (or string in
        its a variable assignment) and the modified variables dictionnary
    """
    varname = None
    # If the equal sign is present, then the expression is a variable assignment (eg. result=1+3)
    # We split the expression into two parts: variable (eg. 'result') and postfix expression (eg. '1+3')
    if "=" in expr:
        varname, expr = expr.split("=")
    try:
        postfix = infix_to_postfix(expr)
        result = eval_postfix(postfix, variables)
    except Exception as exc: # pylint: disable=broad-exception-caught
        result = "E!>" + type(exc).__name__ + ": " + str(exc)
        return result, variables

    variables["ANS"] = result

    # If varname is not None (ie. we assigned a value to it), then store the result in the
    # variables dictionnary
    if varname is not None:
        variables[varname] = result
        result = varname + "=" + str(result)

    # Note that return the variables dictionnary is not strictly necessary as it is passed
    # by reference, but this behaviour can be counter-intuitive
    return result, variables


def main():
    """Main program, this reads from the input file, and outputs result to the output file
    """
    results = []

    # Start with some initial variables
    variables = {
        "PI": 3.14159,
        "e": 2.71828,
        "ANS": None
    }

    with open(IFNAME, "r", encoding="UTF-8") as input_file:
        # For each line in the input file, strip it (remove the trailing \n) and run
        # throught the pipeline add the result to our results list and append a newline for writing
        for line in input_file.readlines():
            # If the line is empty, append a new line to the output (so the files match when
            # side by side) and go to next iteration of the loop
            if line == "\n":
                results.append("\n")
                continue

            result, variables = pipeline(line.rstrip(), variables)
            results.append(str(result) + "\n")

    with open(OFNAME, "w", encoding="UTF-8") as output_file:
        # Write the results into our output file
        output_file.writelines(results)



if __name__ == "__main__":
    main()
