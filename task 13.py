def odd_list(a, n):
    """
    The function returns a list of even values from a list of n integer elements.
    :param a: list of n integer elemets
    :param n: quantity of elements in list
    :return: the list of even values
    """

    if n == 0:
        return a
    else:
        if a[0] % 2 != 0:
            a.remove(a[0])
            return odd_list(a, n-1)
        else:
            return [a[0]] + odd_list(a[1:], n-1)


print(odd_list([6661, 23, 33, 2, 55, 160, 32], 7))
