"""

Longest path in weighted DAG

Given a weighted Directed Acyclic Graph, find the longest path between two given node.
I came up with a simple BFS solution, but then Googled the question after the interview and this seems to be more complicated than what I solved in the interview:

The input is given as a list of String. a-b means the edge from a to b and the weight it has (you don't need to parse the json),


[
    {
        "str": "a-b",
        "weight": 2
    },
    {
        "str": "b-c",
        "weight": 2
    },
        {
        "str": "a-d",
        "weight": 1
    },
        {
        "str": "d-c",
        "weight": 5
    }
]

// the answer is "a -> d -> c" with total weight of 6
You need to implement the following method:

int longestPath(Edge[] edge) {}

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
