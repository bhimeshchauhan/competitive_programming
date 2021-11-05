"""

https://leetcode.com/discuss/interview-question/1376859/Facebook-Puzzle

"""


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    S.sort()
    start, res = 1, 0
    S.append(N+K+1)
    for s in S:
        delta = s-K-start
        if delta > 0:
            res += math.ceil(delta / (K+1))
        start = s+K+1
    return res


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here
    S.sort()

    extra_diner = 0
    # Handle cases to accommodate extra diner between 2 person
    i = 0
    while i < M-1:
        start = S[i] + (K+1)
        end = S[i+1] - (K + 1)
        extra_diner = extra_diner + get_extra_diner(start, end, K)
        i += 1

    extra_diner_start_case = get_extra_diner(1, S[0]-(K+1), K)
    extra_diner_end_case = get_extra_diner(S[-1] + K+1, N, K)

    return extra_diner_start_case + extra_diner + extra_diner_end_case


def get_extra_diner(start, end, K):
    '''
    Diner can occupy start and end
    '''
    if end < start:
        return 0
    seats = end - start + 1

    out = int(seats / (K + 1))
    if seats % (K + 1) != 0:
        out = out + 1
    return out