"""

Knight Proabability in Chessboard

"""

# BFS

import collections


def knightProbability(self, N, K, r, c):
    """
    BFS, use a set to track the nodes in a tree remaining in the board in each step
    Time: O(8 * N ^ 2 * K)
    Space: O(N ^ 2)
    """
    q = {(r, c): 1}
    level = 0
    directions = {(dx, dy) for dx in (-2, -1, 1, 2)
                  for dy in (-2, -1, 1, 2) if abs(dx) + abs(dy) == 3}

    def is_in_board(r, c): return 0 <= r < N and 0 <= c < N
    while level < K and q:
        next_q = collections.defaultdict(int)
        for coord, count in q.items():
            x, y = coord
            for dx, dy in directions:
                if is_in_board(x + dx, y + dy):
                    next_q[(x + dx, y + dy)] += count
        q = next_q
        level += 1
        # print(f'Level {level}: {q}')

    return sum(q.values()) / 8 ** K


# DFS

def knightProbability(self, N, K, r, c):
    """
    dfs with memo
    Time: O(K*N^2)
    Space: O(K*N^2)
    """
    def is_in_board(r, c): return 0 <= r < N and 0 <= c < N
    directions = {(dx, dy) for dx in (-2, -1, 1, 2)
                  for dy in (-2, -1, 1, 2) if abs(dx) + abs(dy) == 3}
    memo = {}

    def dfs(K, r, c):
        nonlocal memo
        if K == 0:
            return 1
        if (K, r, c) in memo:
            return memo[(K, r, c)]

        p = 0
        for dx, dy in directions:
            x, y = r + dx, c + dy
            if is_in_board(x, y):
                p += dfs(K - 1, x, y) / 8
        memo[(K, r, c)] = p
        return p

    return dfs(K, r, c)
