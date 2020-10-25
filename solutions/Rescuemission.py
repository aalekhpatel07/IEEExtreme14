def solve(n, arr, d, days):
    """
    Solve the problem here.
    :return: The expected output.
    """
    prefix = [0 for _ in range(n)]
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]

    def presum(_q, _r):
        assert _r < n
        if _q == 0:
            return prefix[_r]
        return prefix[_r] - prefix[_q-1]

    rescued = 0
    if d == 1:
        l, r, v = days[0]
        return min(presum(l-1, r-1), v)

    for i in range(d):
        l_current, r_current, v_current = days[i]
        val1 = v_current
        val2 = presum(l_current - 1, r_current - 1)
        val3 = prefix[-1] - rescued
        current = max(val1, val2, val3)
        rescued += min(val1, val2 + current, val3)

    return rescued


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.
    """
    n = int(input())
    arr = list(map(int, input().split(' ')))
    d = int(input())
    days_data = []
    for _ in range(d):
        days_data.append(list(map(int, input().split(' '))))
    result = solve(n, arr, d, days_data)
    print(result)
    return result


def main():
    return driver()


if __name__ == '__main__':
    main()
