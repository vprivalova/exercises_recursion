def nod(a, b):
    """
    The function determines the greatest common divisor of the numbers a and b.
    :param a: first natural number
    :param b: second natural number
    :return: the greatest common divisor of the numbers a and b
    """

    if a == b:
        return b
    elif a > b:
        return nod(a-b, b)
    elif a < b:
        return nod(a, b - a)


print(nod(2460, 4420))
