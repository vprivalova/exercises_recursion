def pownum(a, n):
    """
    The function calculates the degree n of a real number a.
    :param a: real number
    :param n: degree
    :return: calculation result
    """
    if n == 0:
        return 1
    elif n > 0:
        return a * pownum(a, n-1)
    elif n < 0:
        return (1 / a) * pownum(a, n + 1)


print(pownum(0.16, -4))
