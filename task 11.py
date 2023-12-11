def ind_maxlist(a):
    """
    The function identifies the index of maximum element from the list of integer elements.
    :param a: list of integer elemets
    :return: index of maximum element
    """

    if len(a) == 1:
        return 0
    else:
        value = ind_maxlist(a[1:]) + 1
        if a[0] > a[value]:
            return 0
        else:
            return ind_maxlist(a[1:]) + 1


print(ind_maxlist([6661, 23, 33, 2, -6, 160, 55]))
