# 4. Median of Two Sorted Arrays

"""

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

"""

"""

"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # odd length -> e.g. length 5, left(2) and right(2) would be the same index
        # even length -> e.g. length 6, left(2) and right(3) would be different indices
        m, n = len(nums1), len(nums2)
        left, right = (m+n-1)//2, (m+n)//2
        return (self.getKth(nums1, nums2, left) + self.getKth(nums1, nums2, right))/2

    def getKth(self, nums1, nums2, k):
        # if one list is exhausted, return the kth index of the other list
        if nums1 == []:
            return nums2[k]
        if nums2 == []:
            return nums1[k]

        # base case
        # k is 0-based, so finding the kth index equals eliminating k length elements.
            # k == 0 means we have eliminated all smaller indices, return the next highest number, which would be the median
        # e.g. to find the third index (k = 3), we eliminate 3 smaller elements (index 0, 1, 2)
        if k == 0:
            return min(nums1[0], nums2[0])

        # find the subarray to be eliminated this iteration
        m, n = len(nums1), len(nums2)
        # 1-based so k + 1
        eliminated_length = min(m, n, (k+1)//2)
        eliminated_index = eliminated_length - 1              # 0-based so - 1
        if nums1[eliminated_index] <= nums2[eliminated_index]:
            nums1 = nums1[eliminated_index+1:]
        else:
            nums2 = nums2[eliminated_index+1:]

        # update k, the number of elements to be eliminated next round
        k -= eliminated_length

        return self.getKth(nums1, nums2, k)


"""



"""


def findMedianSortedArrays(self, A, B):
    l = len(A) + len(B)
    if l % 2 == 1:
        return self.kth(A, B, l // 2)
    else:
        return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.


def kth(self, a, b, k):
    if not a:
        return b[k]
    if not b:
        return a[k]
    ia, ib = len(a) // 2, len(b) // 2
    ma, mb = a[ia], b[ib]

    # when k is bigger than the sum of a and b's median indices
    if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
        if ma > mb:
            return self.kth(a, b[ib + 1:], k - ib - 1)
        else:
            return self.kth(a[ia + 1:], b, k - ia - 1)
    # when k is smaller than the sum of a and b's indices
    else:
        # if a's median is bigger than b's, a's second half doesn't include k
        if ma > mb:
            return self.kth(a[:ia], b, k)
        else:
            return self.kth(a, b[:ib], k)
