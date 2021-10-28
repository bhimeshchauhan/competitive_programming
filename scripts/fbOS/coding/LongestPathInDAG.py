"""

Longest Path in Directed Acyclic Graph

"""

import collections


def adj(edges):  # create adjacency dict and indegree dict
    fr, to = collections.defaultdict(list), collections.defaultdict(int)
    for u, v, w in edges:
        fr[u].append((v, w))
        to[v] += 1
    return fr, to


def longestGiven(edges, src, dst):  # dfs topological dp
    dp, (fr, _) = {}, adj(edges)

    def dfs(u=src):
        if u not in dp:
            dp[u] = max((v != dst and dfs(v)) + w for v, w in fr[u])
        return dp[u]
    return dfs()


def longestDAG(edges):  # bfs topological dp
    dp, (fr, to) = collections.defaultdict(int), adj(edges)
    S = set(fr.keys())
    while S:
        u = S.pop()
        if not to[u]:
            for v, w in fr[u]:
                dp[v] = max(dp[v], dp[u] + w)
                to[v] -= 1
                S.add(v)
    return max(dp.values())
