"""

A cafeteria table consists of a row of N seats, numbered from 1 to N from left to right. Social distancing guidelines require that every diner be seated such that K seats their left and K seats to their right (or all the remaining seats to that side if there are fewer than K) remain empty.

There are currently M diners seated at the table, the ith of whom is in seat Si. No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.

Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
Please take care to write a solution which runs within the time limit.

"""


import math


def getMaxAdditionalDinersCount(N, K, M, S):
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


if __name__ == "__main__":
    # N = 15
    # K = 2
    # M = 3
    # S = [11, 6, 14]

    N = 10
    K = 1
    M = 2
    S = [2, 6]
    print(getMaxAdditionalDinersCount(N, K, M, S))
