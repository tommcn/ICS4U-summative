"""
Helper module, it is a separate file to reduce circular imports
"""

# Type alias for the variable type, it represents a dictionnary with
# string keys (the variable names) and float values (the value of the corresponding
# variable)
VariablesType = dict[str, float]


class VariableNotFound(Exception):
    """
    Signifies that the user is using a variable for which the system as no value
    """


class ImproperExpression(Exception):
    """
    Signifies the user entered an expression that isn't valid
    """
