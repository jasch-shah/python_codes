from collections import defaultdict
from math import inf


def tsp(dists):
    N = len(dists)
    vsets = defaultdict(lambda: inf)
    pre = defaultdict(lambda: inf)
    for i in range(1, N):
        pre[((1 << i) + 1, i)] = dists[0][i]
    for _ in range(2, N):
        for vs, j in pre:
            for i in range(1, N):
                if ((1<<i) & vs) == 0:
                    vsets[(vs | (1<<i), i)] = min(vsets[(vs | (1<<i), i)],
                                                  pre[(vs, j)] + dists[j][i])
        pre = vsets
        vsets = defaultdict(lambda: inf)
    return min(dists[k[1]][0] + v for k, v in pre.items())


def solve_from_input():
    t = int(input().strip())
    for _ in range(t):
        N = int(input().strip())
        _dists = [int(d) for d in input().split()]
        dists = [_dists[i:i+N] for i in range(0, N*N, N)]
        print(tsp(dists))

solve_from_input()