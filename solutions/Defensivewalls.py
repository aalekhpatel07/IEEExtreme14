def solve(n, points):
    """
    Solve the problem here.
    :return: The expected output.
    """
    
    return 0


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.
    """
    n = int(input())
    points = []
    for _ in range(n):
        points.append(list(map(int, input())))

    result = solve(n, points)
    print(result)
    return result


def main():
    return driver()


if __name__ == '__main__':
    main()
