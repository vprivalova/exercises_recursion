def fib(k):
    """
    The function defines the k-th element of the Fibonacci sequence.
    :param k: number of required element
    :return: k-th element of the Fibonacci sequence
    """

    if k == 1:
        return 1
    elif k == 2:
        return 1
    else:
        return fib(k-1) + fib(k-2)


print(fib(20))
