"""
Explanation
Count the elements with Counter
If k > 0, for each element i, check if i + k exist.
If k == 0, for each element i, check if count[i] > 1


Explanation
Time O(N)
Space O(N)

"""
import collections


def findPairs1(nums, k):
    # Initialize result
    res = 0
    # Counter method to count items
    c = collections.Counter(nums)
    # For each number in the array of counters
    for i in c:
        # If the difference is not zero and sum of current item and
        # the difference and
        # the value of the current item is greater than one
        if k > 0 and i + k in c or k == 0 and c[i] > 1:
            # increment result
            res += 1
    return res


# which equals to:

def findPairs2(nums, k):
    c = collections.Counter(nums)
    return sum(k > 0 and i + k in c or k == 0 and c[i] > 1 for i in c)


print(findPairs1([3, 1, 4, 1, 5], 2))
print(findPairs2([3, 1, 4, 1, 5], 2))
