from math import inf

def solve(queries):
    """
    Solve the problem here.
    :return: The expected output.
    """
    def is_int(num):
        epsilon = 1e-9
        return abs(int(num) - num) < epsilon

    result = []

    for c, h, g in queries:
        if c == 0 and h == 0 and g > 0:
            if g % 2 == 0:
                result.append(g // 2)
            else:
                result.append(1 + g // 2)
            continue
        if g == 0 and h == 0 and c > 0:
            result.append(c)
            continue
        if c == 0 and g == 0 and h > 0:
            if h % 2 == 0:
                result.append(h // 2)
            else:
                result.append(h // 2 + 1)
            continue

        best = inf
        for dc in range(-25, 25):
            for dh in range(-25, 25):
                for dg in range(-25, 25):
                    x = -(c + dc) + (1/4)*(h + dh) + (1/2)*(g + dg)
                    y = (1/4)*(-h - dh + 2*g + 2*dg)
                    z = (1/24)*(4*c + 4*dc + h + dh - 2*g - 2*dg)
                    if is_int(x) and is_int(y) and is_int(z):
                        abs_sum = abs(dc) + abs(dh) + abs(dg)
                        if abs_sum <= best:
                            best = abs_sum
        result.append(best)
    return result


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.
    """
    # a, b = list(map(int, input().split(' ')))
    t = int(input())
    queries = []
    for _ in range(t):
        c, h, o = list(map(int, input().split(' ')))
        queries.append((c, h, o))
    result = solve(queries)
    print('\n'.join(map(str, result)))
    return result


def main():
    return driver()


if __name__ == '__main__':
    main()
