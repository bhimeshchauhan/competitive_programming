"""

Find Median from Data Stream

The median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value and 
the median is the mean of the two middle values.

- For example, for arr = [2,3,4], the median is 3.
- For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the 
data stream to the data structure.
- double findMedian() returns the median of all elements 
so far. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]

Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0 

Constraints:

- -105 <= num <= 105
- There will be at least one element in the data structure before calling findMedian.
- At most 5 * 104 calls will be made to addNum and findMedian.

Follow up:

- If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
- If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

"""

# Simple Sorting

"""

Algorithm

- Store the numbers in a resize-able container. Every time you need to output the median, 
sort the container and output the median.

"""

"""

Complexity Analysis

Time complexity: O(nlogn) + O(1) ≃ O(nlogn)

Adding a number takes amortized O(1)O(1) time for a container with an efficient resizing scheme.
Finding the median is primarily dependent on the sorting that takes place. This takes 
O(nlogn) time for a standard comparative sort.

Space complexity: O(n) linear space to hold input in a container. 
No extra space other than that needed 
(since sorting can usually be done in-place).

"""

# Two heap solution

"""

Complexity Analysis

Time complexity: O(5⋅logn)+O(1)≈O(logn).

At worst, there are three heap insertions and two heap deletions from the top. Each of these takes about 
O(logn) time. Finding the median takes constant O(1) time since the tops of heaps are directly accessible.

Space complexity: O(n) linear space to hold input in containers.

"""

from heapq import *


class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])