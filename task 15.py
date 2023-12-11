def convertation(x, digits):
    if x == 0:
        return digits
    else:
        digits.append(x % 2)
        convertation(x // 2, digits)


def ten_to_bin(x):
    """
    The function converts a number from decimal to binary.
    :param x: decimal number
    :return: binary number
    """
    result = []
    binary = ''
    convertation(x, result)
    result.reverse()
    for elem in result:
        binary = binary + str(elem)
    return binary


print(ten_to_bin(123))
