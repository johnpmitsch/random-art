import random


def avg(x, y):
    return x / y

def avg_exp():
    return 'avg('+ generate_expression(), generate_expression() + ')'

def sin():
    return 'sin(' + generate_expression() + ')'

def cos():
    return 'cos(' + generate_expression() + ')'

def generate_expression(probability=0.99):
    expr_list = [sin(),
                 avg_exp(),
                 cos()
                 ]
    if random.random() < probability:
        return expr_list[random.randint(0,3)]
    else:
        return 'x'

print(generate_expression())
