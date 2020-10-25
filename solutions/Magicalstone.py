def solve(n, mp, q, queries):
    """
    Solve the problem here.
    :return: The expected output.
    """
    def set_transform(s):
        return {mp[i] - 1 for i in s}

    def stringify(tup):
        return ','.join(map(str, tup))

    answer = [-1 for _ in range(n-1)] + [0]

    current = {i for i in range(n)}
    visited = set()
    steps = 0

    while stringify(tuple(sorted(current))) not in visited:
        visited |= {stringify(tuple(sorted(current)))}
        current = set_transform(current)
        steps += 1
        if answer[len(current)-1] == -1:
            answer[len(current)-1] = steps

    return [answer[z-1] for z in queries]


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.
    """
    n = int(input())
    mp = list(map(int, input().split(' ')))
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(int(input()))
    result = solve(n, mp, q, queries)
    print('\n'.join(map(str, result)))
    return result


def main():
    return driver()


if __name__ == '__main__':
    main()
