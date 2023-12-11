def sum_progress(a1, r, n):
    """
    The function finds the sum of the progression consisted of n elements.
    :param a1: first element of the progression
    :param r: difference of the progression
    :param n: number of the required element
    :return: sum of the progression consisted of n elements
    """

    if n == 0:
        return 0
    else:
        return a1 + sum_progress(a1+r, r, n-1)


print(sum_progress(18, 23, 61))
