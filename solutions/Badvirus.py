from math import inf
from queue import Queue


def _biconnected_dfs(adj, components=True):
    # depth-first search algorithm to generate articulation points
    # and biconnected components
    visited = set()
    for start in adj:
        if start in visited:
            continue
        discovery = {start: 0}  # time of first discovery of node during search
        low = {start: 0}
        root_children = 0
        visited.add(start)
        edge_stack = []
        stack = [(start, start, iter(adj[start]))]
        while stack:
            grandparent, parent, children = stack[-1]
            try:
                child = next(children)
                if grandparent == child:
                    continue
                if child in visited:
                    if discovery[child] <= discovery[parent]:  # back edge
                        low[parent] = min(low[parent], discovery[child])
                        if components:
                            edge_stack.append((parent, child))
                else:
                    low[child] = discovery[child] = len(discovery)
                    visited.add(child)
                    stack.append((parent, child, iter(adj[child])))
                    if components:
                        edge_stack.append((parent, child))

            except StopIteration:
                stack.pop()
                if len(stack) > 1:
                    if low[parent] >= discovery[grandparent]:
                        if components:
                            ind = edge_stack.index((grandparent, parent))
                            yield edge_stack[ind:]
                            edge_stack = edge_stack[:ind]
                        else:
                            yield grandparent
                    low[grandparent] = min(low[parent], low[grandparent])
                elif stack:  # length 1 so grandparent is root
                    root_children += 1
                    if components:
                        ind = edge_stack.index((grandparent, parent))
                        yield edge_stack[ind:]
        if not components:
            # root node is articulation point if it has more than 1 child
            if root_children > 1:
                yield start


def bfs(adjacency, n, start):
    distances = {i: inf for i in adjacency}
    q = Queue()
    q.put(start)
    distances[start] = 0

    while not q.empty():
        current = q.get()
        for nbs in adjacency[current]:
            if distances[nbs] > distances[current] + 1:
                distances[nbs] = distances[current] + 1
                q.put(nbs)
    return distances


def solve(n, edges, terminals):
    """
    Solve the problem here.
    :return: The expected output.
    """
    adjacency = dict()
    for start, end in edges:
        if start in adjacency:
            adjacency[start] |= {end}
        else:
            adjacency[start] = {end}
        if end in adjacency:
            adjacency[end] |= {start}
        else:
            adjacency[end] = {start}

    answer = []
    bi_comps = [comp for comp in _biconnected_dfs(adjacency, n)]

    if len(bi_comps) == 1:
        return [2 for _ in range(len(terminals))]

    cut_vertices = set()
    for x in range(len(bi_comps)):
        for y in range(len(bi_comps)):
            cmp_set_x = set()
            for z_s, z_e in bi_comps[x]:
                cmp_set_x |= {z_s}
                cmp_set_x |= {z_e}
            cmp_set_y = set()
            for z_s, z_e in bi_comps[y]:
                cmp_set_y |= {z_s}
                cmp_set_y |= {z_e}
            r_set = cmp_set_x.intersection(cmp_set_y)
            if len(list(r_set)) == 1:
                cut_vertices |= {r_set.pop()}

    cv_distances = dict()
    for v in cut_vertices:
        cv_distances[v] = bfs(adjacency, n, v)

    for t_start, t_end in terminals:
        # temp_adj = {x: {y for y in adjacency[x]} for x in adjacency}
        # temp_adj[terminal_start] |= {terminal_end}
        # temp_adj[terminal_end] |= {terminal_start}
        # print(cut_vertices)

        distances = bfs(adjacency, n, t_start)
        just_added = False

        for comp in bi_comps:
            cmp_set = set()
            for z_s, z_e in comp:
                cmp_set |= {z_s}
                cmp_set |= {z_e}

            if t_start in cmp_set and t_end in cmp_set:
                just_added = True
                answer.append(2)

        if just_added:
            continue

        count = 2

        for art in cut_vertices:
            if cv_distances[art][t_start] + cv_distances[art][t_end] <= distances[t_end]:
                count += 1
        answer.append(count)
    return answer


def driver():
    """
    Make sure this driver returns the result.
    :return: result - Result of computation.
    """
    n, m = list(map(int, input().split(' ')))
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split(' '))))
    scenarios = int(input())
    source_dest_pairs = []
    for _ in range(scenarios):
        source_dest_pairs.append(tuple(map(int, input().split(' '))))
    result = solve(n, edges, source_dest_pairs)
    print('\n'.join(map(str, result)))
    return result


def main():
    return driver()


if __name__ == '__main__':
    main()
