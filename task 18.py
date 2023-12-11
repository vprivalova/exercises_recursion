def symmetry_checking(sbstr, n):
    if sbstr[0] != sbstr[-1]:
        return False
    elif n == 0:
        return True
    else:
        return symmetry_checking(sbstr[1:-1], n-1)


def simmetr(s, i, j):
    """
    The function identifies whether the part of string s starting with the i-th character
    and ending with the j-th character is symmetric.
    :param s: string
    :param i: index of beggining of substring
    :param j:index of ending of substring
    :return:True if substring is symmetric and False if not
    """

    substring = s[i:j+1]
    n = len(substring) // 2
    if symmetry_checking(substring, n) is True:
        return True
    else:
        return False


print(simmetr('msokssoksm', 3, 7))
