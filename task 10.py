def max_list(a):
    """
    The function identifies the maximum element from the list of integer elements.
    :param a: list of integer elemets
    :return: maximum element
    """

    if len(a) == 1:
        return a[0]
    else:
        if a[0] > a[1]:
            a.remove(a[1])
        else:
            a.remove(a[0])
        return max_list(a)


print(max_list([1, 523, 33, 2, -6, 10, 55]))
