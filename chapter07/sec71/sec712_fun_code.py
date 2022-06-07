# coding = utf8

import math

def eq12_fun_code():
    """
    >>> def eq12(a, b, c):
    ...     delta = b**2 - 4*a*c
    ...     if delta >= 0:
    ...         x1 = (-b + math.sqrt(delta)) / (2*a)
    ...         x2 = (-b - math.sqrt(delta)) / (2*a)
    ...     else:
    ...         x1 = complex(-b, math.sqrt(-delta)) / (2*a)
    ...         x2 = complex(-b, - math.sqrt(-delta)) / (2*a)
    ...     return x1, x2
    >>> eq12(1, 2, 3)
    ((-1+1.4142135623730951j), (-1-1.4142135623730951j))
    """
    pass
