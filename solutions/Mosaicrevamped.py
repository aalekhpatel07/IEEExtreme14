from math import ceil


def solve(w, h, a, b, m, c):
    """
    Solve the problem here.
    :return: The expected output.
    """

    full_tiles_needed = ceil(h / b) * ceil(w / a)
    piles_needed = ceil(full_tiles_needed / 10)
    tiles_cost = piles_needed * m

    cutting_cost = 0
    if w % a == 0:
        if h % b == 0:
            pass
        else:
            cutting_cost = w
    else:
        if h % b == 0:
            cutting_cost = h
        else:
            cutting_cost = w + h

    return tiles_cost + c * cutting_cost


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.
    """
    w, h, a, b, m, c = list(map(int, input().split(' ')))
    result = solve(w, h, a, b, m, c)
    print(result)
    return result


def main():
    return driver()


if __name__ == '__main__':
    main()
