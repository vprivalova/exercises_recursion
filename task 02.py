def count(n):
    """
    The function counts the number of digits.
    :param n: natural number
    :return: quantity of digits in number
    """

    if n == 0:
        return 0
    else:
        return count(n // 10) + 1


print(count(0))
