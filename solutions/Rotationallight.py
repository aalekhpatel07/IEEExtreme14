def solve(n, t, indices):
    """
    Solve the problem here.
    :return: The expected output.
    """
    def make_jump(arr, j):
        for z in range(len(arr)):
            arr[z] = (arr[z] + j) % t
        return arr

    def rotate_right(arr):
        return [arr[-1]] + arr[0:len(arr) - 1]
    indices = [indices[z] - indices[0] for z in range(len(indices))]
    to_compare = [indices[z] for z in range(len(indices))]
    total = 0

    while True:
        jump = t - to_compare[-1]
        total += jump
        to_compare = rotate_right(make_jump(to_compare, jump))
        if to_compare == indices:
            break

    return total - 1


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.
    """
    n, t = list(map(int, input().split(' ')))

    indices = list(map(int, input().split(' ')))

    result = solve(n, t, indices)
    print(result)
    return result


def main():
    return driver()


if __name__ == '__main__':
    main()
