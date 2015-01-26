import random
from math import sin, cos, pi

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.

def avg(x,y):
    return x/y



def get_expression():
    """returns a mathematical expression from a dictionary index"""

    expr_dict = {'sin': lambda x, y: sin(sin(pi * x) + cos(pi * x)),
                 'cos': lambda x, y: cos(pi * x),
                 'J': lambda x, y: sin(sin(x+y)),
                 'O': lambda x, y: sin(pi * x) * y,
                 'H': lambda x, y: cos(pi * y) * x,
                 'N': lambda x, y: cos(pi * ((y * y) * cos(pi * x))),
                 'M': lambda x, y: avg(avg(sin(pi * cos(pi * sin(pi * cos(pi * x)))), sin(pi * y)),cos(pi * y)),
                 'I': lambda x, y: sin(sin(cos(sin(sin(sin(sin(sin(x * pi * y * pi))))))))
                 }

    return random.choice(list(expr_dict.values()))


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""

    expr = get_expression()

    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
