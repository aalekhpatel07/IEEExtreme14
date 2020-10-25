from math import inf


def solve(positive, negative):
    """
    Solve the problem here.
    :return: The expected output.
    """


    pos_slope = []
    # Line through origin so y = mx.
    for (x, y) in positive:
        if x == 0:
            pos_slope.append(inf)
        else:
            pos_slope.append(y/x)

    neg_slope = []
    # Line through origin so y = mx.
    for (x, y) in negative:
        if x == 0:
            neg_slope.append(inf)
        else:
            neg_slope.append(y/x)

    if min(len(negative), len(positive)) == 0:
        if len(negative) == 0:
            # only positive points.
            smallest_positive_slope = min(x for x in pos_slope if x > 0)

            pass
        else:
            pass



    return 'YES' if (min(pos_slope) >= max(neg_slope) ) else 'NO'


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.
    """
    t = int(input())
    for _ in range(t):
        positive = []
        negative = []
        n = int(input())
        for z in range(n):
            x, y, sign = list(map(float, input().split(' ')))
            if sign > 0:
                positive.append((x, y))
            else:
                negative.append((x, y))

        result = solve(positive, negative)
        print(result)
    return


def main():
    return driver()


if __name__ == '__main__':
    main()
