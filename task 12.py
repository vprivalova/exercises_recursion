def search(a, x):
    """
    The function identifies whether there is a number x among the integer values of the list.
    :param a: list of integer numbers
    :param x: the number to be checked
    :return: 1 if x is in list a or 0 if x is not in list a
    """

    if len(a) == 1 and a[0] == x:
        return 1
    elif len(a) == 1 and a[0] != x:
        return 0
    else:
        if a[0] != x:
            a.remove(a[0])
        else:
            a.remove(a[1])
        return search(a, x)


print(search([6661, 23, 33, 2, -6, 160, 55], -6))
