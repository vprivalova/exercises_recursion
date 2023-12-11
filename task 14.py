def numbers(x):
    """
    The function prints the digits of the natural number x on the screen in reverse order.
    :param x: natural number
    :return: None
    """

    if x == 0:
        return None
    else:
        print(x % 10)
        numbers(x//10)


numbers(1234)
