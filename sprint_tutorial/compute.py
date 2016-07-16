""" Module to compute stuff
"""


def my_sum(x, y):
    """ Compute the sum of 2 numbers, as a float.
    """
    return (x + y)*1.0


def my_power(a,n):
    """ Compute a^n """
    pow = a
    for i in range(n-1):
        pow = pow*a

    return pow
