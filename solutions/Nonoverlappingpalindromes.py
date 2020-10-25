def solve(words):
    """
    Solve the problem here.
    :return: The expected output.
    """
    answers = []
    for word in words:
        if len(word) == 2:
            answers.append(2)
        else:
            best = 1
            for i in range(1, len(word)):
                left = word[0:i]
                right = word[i:]
                left_pal = manachers_algorithm(left)
                right_pal = manachers_algorithm(right)
                best = max(best, len(left_pal) + len(right_pal))
            answers.append(best)
    return answers


def add_boundaries(s):
    if s is None or len(s) == 0:
        return '||'
    return '|' + '|'.join(map(str, [s[i] for i in range(len(s))])) + '|'


def remove_boundaries(s):
    if s is None or len(s) < 3:
        return ''
    return s.replace('|', '')


def manachers_algorithm(s):
    if s is None or len(s) == 0:
        return ''

    dummy = add_boundaries(s)
    p = [0 for _ in range(len(dummy))]
    c, r, m, n = 0, 0, 0, 0
    for i in range(1, len(dummy)):
        if i > r:
            p[i] = 0
            m = i - 1
            n = i + 1
        else:
            i2 = 2*c - i
            if p[i2] < r-i-1:
                p[i] = p[i2]
                m = -1
            else:
                p[i] = r-i
                n = r+1
                m = 2*i - n
        while m >= 0 and n < len(dummy) and dummy[m] == dummy[n]:
            p[i] += 1
            m -= 1
            n += 1
        if i + p[i] > r:
            c = i
            r = i + p[i]
    q, z = 0, 0
    for i in range(1, len(dummy)):
        if q < p[i]:
            q = p[i]
            z = i

    dummy_copy = [a for a in dummy[z-q: z+q+1]]
    return remove_boundaries(''.join(map(str, dummy_copy)))


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.
    """
    # a, b = list(map(int, input().split(' ')))
    t = int(input())
    words = []
    for i in range(t):
        words.append(input())

    result = solve(words)
    print('\n'.join(map(str, result)))
    return result


def main():
    return driver()


if __name__ == '__main__':
    main()
