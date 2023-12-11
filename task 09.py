def combin(n, k):
    """
    The function calculates the combination of k elements from n.
    :param n: total number of elements
    :param k:  number of selectable elemets
    :return: amount of combinations
    """

    if k == 0:
        return 1
    if k == n:
        return 1
    else:
        return combin(n-1, k) + combin(n-1, k-1)


print(combin(8, 5))
