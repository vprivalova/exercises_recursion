def convertation(x, n, digits):
    if x == 0:
        return digits
    else:
        digits.append(x % n)
        convertation(x // n, n, digits)


def ten_to_n(x, n):
    """
    The function converts a number from decimal to another n-number system.
    :param x: decimal number
    :param n: base of number system
    :return: number in the new number system
    """
    result = []
    n_number = ''
    convertation(x, n, result)
    result.reverse()
    for elem in result:
        if elem == 10:
            elem = 'A'
        elif elem == 11:
            elem = 'B'
        elif elem == 12:
            elem = 'C'
        elif elem == 13:
            elem = 'D'
        elif elem == 14:
            elem = 'E'
        elif elem == 15:
            elem = 'G'
        n_number = n_number + str(elem)
    return n_number


print(ten_to_n(12283, 13))
