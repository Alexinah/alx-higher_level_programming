#!/usr/bin/python3


def safe_print_division(a, b):
    """ Divides two integrs and prints the result

    Args: a , b

    Results: Print on the finally
    Return value of division
    otherwise: none
    """
    try:
        sol = a / b
    except (TypeError, ZeroDivisionError):
        sol = None
    finally:
        print("Inside result: {}".format(sol))
        return (sol)
