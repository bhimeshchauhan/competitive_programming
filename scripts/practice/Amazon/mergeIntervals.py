"""

Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""

"""

Complexity Analysis

Time complexity : O(nlogn)
Other than the sort invocation, we do a simple linear scan of the list, so the runtime 
is dominated by the O(nlogn) complexity of sorting.

Space complexity : O(logN) (or O(n))
If we can sort intervals in place, we do not need more than constant 
additional space, although the sorting itself takes O(logn) space. 
Otherwise, we must allocate linear space to store a copy of 
intervals and sort that.

"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedIntervals = sorted(intervals)
        res = [sortedIntervals[0]]
        for start, end in sortedIntervals:
            if res and start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res
