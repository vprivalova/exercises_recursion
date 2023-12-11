def mod_number(a, b):
    """
    The function finds the remainder from dividing the natural number a by the natural number b.
    :param a: divident
    :param b: divider
    :return: remainder of division
    """

    if a < b:
        return a
    else:
        return mod_number(a - b, b)


print(mod_number(673, 18))
