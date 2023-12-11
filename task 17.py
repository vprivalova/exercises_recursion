def prime_checking(x, n):
    if n == 1:
        return True

    if x % n == 0:
        return False
    else:
        return prime_checking(x, n-1)


def function1(x):
    """
    Function is identifying whether the number is prime or not.
    :param x: number for checking
    :return: 1 if number is prime and 0 if not
    """
    dividers = x - 1
    if prime_checking(x, dividers) is True:
        return 1
    else:
        return 0


print(function1(101))
