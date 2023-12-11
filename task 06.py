def degree5(n):
    """
    The function calculates what degree of the number 5 is the number n.
    :param n: natural number
    :return: required degree or '-1' if n is not a degree of the number 5
    """

    if n == 1:
        return 0

    elif n % 5 != 0:
        return -1

    elif n % 5 == 0:
        value = degree5(n/5)

        if value != -1:
            return 1 + degree5(n/5)
        else:
            return -1


print(degree5(225))
print(degree5(125))
