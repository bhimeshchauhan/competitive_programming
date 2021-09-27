"""

Find the Number Occurring Odd Number of Times

Given an array of positive integers. All numbers occur 
an even number of times except one number which occurs 
an odd number of times. Find the number in O(n) time 
& constant space.

Examples : 

Input : arr = {1, 2, 3, 2, 3, 1, 3}
Output : 3

Input : arr = {5, 7, 2, 7, 5, 2, 5}
Output : 5

"""

# importing counter from collections
from collections import Counter

# Python3 implementation to find
# odd frequency element


def oddElement(arr, n):

    # Calculating frequencies using Counter
    count_map = Counter(arr)

    for i in range(0, n):

        # If count of element is odd we return
        if (count_map[arr[i]] % 2 != 0):
            return arr[i]


# Driver Code
if __name__ == "__main__":

    arr = [1, 1, 3, 3, 5, 6, 6]
    n = len(arr)
    print(oddElement(arr, n))
