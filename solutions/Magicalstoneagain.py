def solve(n, white, black):
    def set_transform(s, color):
        return {color[i] - 1 for i in s}

    def stringify(tup):
        return ','.join(map(str, tup))

    memo = dict()
    current = {i for i in range(n)}
    res = ''
    try:
        val = dfs(current, white, black, memo, set_transform, stringify)
        return val
    except RecursionError as e:
        return ''


def dfs(node, white, black, memo, apply, stringify):
    s = ''
    stack = [(tuple(node), s)]
    i = 0
    while len(stack) > 0:
        if i > 1750:
            break
        i += 1
        current = stack[-1]
        del stack[-1]
        curr_set, s = set(current[0]), current[1]
        if len(curr_set) == 1:
            return s
        else:
            whitened = apply(curr_set, white)
            blackened = apply(curr_set, black)
            if len(blackened) <= len(whitened):
                if (stringify(curr_set), 0) not in memo:
                    memo[(stringify(curr_set), 0)] = whitened
                    stack.append((tuple(whitened), s + 'W'))
                if (stringify(curr_set), 1) not in memo:
                    memo[(stringify(curr_set), 1)] = blackened
                    stack.append((tuple(blackened), s + 'B'))
            else:
                if (stringify(curr_set), 1) not in memo:
                    memo[(stringify(curr_set), 1)] = blackened
                    stack.append((tuple(blackened), s + 'B'))
                if (stringify(curr_set), 0) not in memo:
                    memo[(stringify(curr_set), 0)] = whitened
                    stack.append((tuple(whitened), s + 'W'))

    return 'impossible'


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.
    """
    t = int(input())
    result = []
    for _ in range(t):
        n = int(input())
        white = list(map(int, input().split(' ')))
        black = list(map(int, input().split(' ')))
        answer = solve(n, white, black)
        result.append(answer)

    print('\n'.join(map(str, result)))
    return result


def main():
    return driver()


if __name__ == '__main__':
    main()
