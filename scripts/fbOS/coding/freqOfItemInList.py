"""

Frequency of Items In subsequence of List

Given an array of integers arr and a positive integer m, your task is to find the frequency of the most common element within each contiguous subarray of length m in arr.
Return an array of these highest frequencies among subarray elements, ordered by their corresponding subarray's starting index.

Input: [1,2,3,1,2,4,1,4,4], m = 4
Output: [2,2,1,2,2,3]

Input:[1,2], m = 2
Output:[1]

"""

from collections import defaultdict, Counter


def high_freq(arr, m):
    d = defaultdict(int)
    for i in range(m):
        d[arr[i]] += 1
    max_freq = max(d.values())
    inv_freq = defaultdict(set)
    for k, v in d.items():
        inv_freq[v].add(k)
    r = [max_freq]
    for i in range(len(arr)-m):
        inv_freq[d[arr[i]]].remove(arr[i])
        d[arr[i]] -= 1
        inv_freq[d[arr[i]]].add(arr[i])
        if arr[i+m] in inv_freq[d[arr[i+m]]]:
            inv_freq[d[arr[i+m]]].remove(arr[i+m])
        d[arr[i+m]] += 1
        inv_freq[d[arr[i+m]]].add(arr[i+m])
        if d[arr[i+m]] > max_freq:
            max_freq += 1
        elif len(inv_freq[max_freq]) == 0:
            max_freq -= 1
        r.append(max_freq)
    return r


if __name__ == "__main__":
    print(high_freq([1, 2, 3, 1, 2, 4, 1, 4, 4], 4))
