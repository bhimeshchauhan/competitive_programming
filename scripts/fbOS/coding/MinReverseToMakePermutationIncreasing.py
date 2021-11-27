"""

Minimizing Permutations

In this problem, you are given an integer N, and a permutation, P of the integers from 1 to N, denoted as (a_1, a_2, ..., a_N). You want to rearrange the elements of the permutation into increasing order, repeatedly making the following operation:
Select a sub-portion of the permutation, (a_i, ..., a_j), and reverse its order.
Your goal is to compute the minimum number of such operations required to return the permutation to increasing order.

Signature

int minOperations(int[] arr)
Input
Array arr is a permutation of all integers from 1 to N, N is between 1 and 8

Output
An integer denoting the minimum number of operations required to arrange the permutation in increasing order
Example
If N = 3, and P = (3, 1, 2), we can do the following operations:
Select (1, 2) and reverse it: P = (3, 2, 1).
Select (3, 2, 1) and reverse it: P = (1, 2, 3).
output = 2

"""

import collections
def minOperations(arr):
    target = "".join([str(num) for num in sorted(arr)])
    curr = "".join([str(num) for num in arr])
    # In the queue we store (<level>, <permutation>)
    queue = collections.deque([(0, curr)])
    visited = set([curr])

    while queue:
        level, curr = queue.popleft()

        if curr == target:
            return level  # We are done

        for i in range(len(curr)):
            for j in range(i, len(curr)):
                # Reverse elements between i and j (inclusive)
                # Note we are operating on strings here, so we create a new copy
                permutation = curr[:i] + curr[i:j + 1][::-1] + curr[j + 1:]

                if permutation not in visited:
                    visited.add(permutation)
                    queue.append((level + 1, permutation))

    return -1


if __name__ == "__main__":
    print(minOperations([3, 1, 2]))  # 2
    print(minOperations([1, 2, 3]))  # 0
