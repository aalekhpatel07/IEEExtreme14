def solve(c, n, p, w):
    """
    Solve the problem here.
    :return: The expected output.
    """
    if c > w:
        return 0

    leading_ps = w // p
    tables = 0

    zeroes_available = n - (leading_ps + 1)

    if w % p == 0:
        zeroes_available += 1
    while zeroes_available > 0:
        number_of_zeroes_filled = min(w // c,  zeroes_available)

        # w % p
        chips_used = number_of_zeroes_filled * c
        # first chip drawn from the non-zero entry if exists.
        chips_used -= (w % p)

        w -= number_of_zeroes_filled * c
        tables += number_of_zeroes_filled

        if number_of_zeroes_filled < zeroes_available:
            return tables

        zeroes_available = 1 + chips_used // p

    # now assume no zeroes available already.





    return tables


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.
    """
    c, n, p, w = list(map(int, input().split(' ')))
    result = solve(c, n, p, w)
    print(result)
    return result


def main():
    return driver()


if __name__ == '__main__':
    main()
