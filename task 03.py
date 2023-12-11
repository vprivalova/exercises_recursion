def progress(a1, r, n):
    """
    The function finds the n-th element of the progression.
    :param a1: first element of the progression
    :param r: difference of the progression
    :param n: number of the required element
    :return: n-th element of the progression
    """

    if n == 1:
        return a1
    else:
        return r + progress(a1, r, n-1)


print(progress(18, 23, 61))
