from queue import PriorityQueue
from math import inf


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


def neighbors(x, y, n, k, stable):
    for i in range(-k-20, k+20):
        for j in range(-k-20, k+20):
            if is_valid(x-i, y-j, n) and (abs(x-i) + abs(y-j) <= k) and (x-i, y-j) in stable and (x-i, y-j) != (x, y):
                print(x-i, y-i)
                yield x-i, y-j


def heuristic(s_x, s_y, e_x, e_y):
    return abs(s_x - e_x) + abs(s_y - e_y)


def a_star(s_x, s_y, e_x, e_y, n, k, h, stable):

    track = dict()

    g_score = {(s_x, s_y): 0}
    f_score = {(s_x, s_y): h(s_x, s_y, e_x, e_y)}

    pq = PriorityQueue()
    pq.put((0, (s_x, s_y)))

    while not pq.empty():
        curr_dist, curr_coord = pq.get()

        if curr_coord == (e_x, e_y):
            return g_score[(e_x, e_y)], track
        curr_x, curr_y = curr_coord

        for (a, b) in neighbors(curr_x, curr_y, n, k, stable):

            wt = heuristic(a, b, curr_x, curr_y)
            tentative_g_score = g_score[curr_x, curr_y] + wt
            if (a, b) in g_score:
                if tentative_g_score < g_score[a, b]:
                    track[a, b] = (curr_x, curr_y)
                    g_score[a, b] = tentative_g_score
                    f_score[a, b] = g_score[a, b] + h(a, b, e_x, e_y)
                    pq.put((g_score[a, b], (a, b)))
            else:
                track[a, b] = (curr_x, curr_y)
                g_score[a, b] = tentative_g_score
                g_score[a, b] = g_score[a, b] + h(a, b, e_x, e_y)
                pq.put((g_score[a, b], (a, b)))
    if (e_x, e_y) in g_score:
        return g_score[e_x, e_y], track
    else:
        return inf, dict()


def solve(n, stable, queries):
    """
    Solve the problem here.
    :return: The expected output.
    """
    result = []
    for s, t, k in queries:
        s_x, s_y = stable[s-1]
        e_x, e_y = stable[t-1]
        dist, track = a_star(s_x, s_y, e_x, e_y, n, k, heuristic, stable)
        # print(dist)
        if dist == inf:
            result.append(0)
        else:
            result.append(1)
    return result


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.
    """
    n, q, s_q, m_k = list(map(int, input().split(' ')))
    stable = []
    for _ in range(n):
        stable.append(tuple(map(int, input().split(' '))))

    a_s, b_s, c_s, a_t, b_t, c_t, a_k, b_k, c_k = list(map(int, input().split(' ')))

    queries = []

    for i in range(s_q):
        queries.append(list(map(int, input().split(' '))))

    for i in range(s_q + 1, q + 1):
        s_i_minus_1, t_i_minus_1, k_i_minus_1 = queries[i - 1]
        s_i_minus_2, t_i_minus_2, k_i_minus_2 = queries[i - 2]

        current_s_i = (a_s * s_i_minus_1 + b_s * s_i_minus_2 + c_s) % (n+1)
        current_t_i = (a_t * t_i_minus_1 + b_t * t_i_minus_2 + c_t) % (n + 1)
        current_k_i = (a_k * k_i_minus_1 + b_k * k_i_minus_2 + c_k) % m_k
        queries.append((current_s_i, current_t_i, current_k_i))

    result = solve(n, stable, queries)
    i = 2
    total = 0
    prime = int(1e9 + 7)
    for j in range(q):
        total += (i * result[j]) % prime
        i *= 2

    print(total % prime)
    return total % prime


def main():
    return driver()


if __name__ == '__main__':
    main()
