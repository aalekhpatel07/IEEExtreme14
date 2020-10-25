from math import ceil


def solve(b, p, arr):
    """
    Solve the problem here.
    :return: The expected output.
    """
    black = sum([x[0] for x in arr])
    pink = sum([x[1] for x in arr])

    return ceil(black / 10) * b + ceil(pink / 10) * p


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.
    """
    n, b, p = list(map(int, input().split(' ')))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split(' '))))
    result = solve(b, p, arr)
    print(result)
    return result


def main():
    return driver()


if __name__ == '__main__':
    main()
