def count(a, b):
    """
    The function counts the number of squares that can be cut off from a rectangle with sides a and b,
    if the largest square is cut off each time.
    :param a: first side lenth
    :param b: second side length
    :return: amount of squares
    """
    if a == b:
        return 1
    else:
        if a > b:
            return 1 + count(a-b, b)
        else:
            return 1 + count(a, b-a)


print(count(36, 8))
