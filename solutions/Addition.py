def solve(a, b):
    return a + b


def driver():
    a, b = list(map(int, input().split(' ')))
    result = solve(a, b)
    print(solve(a, b))
    return result


def main():
    return driver()


if __name__ == '__main__':
    main()
