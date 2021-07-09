"""

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array
of the non-overlapping intervals that cover all the intervals in the input.

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


class Solution:
	
	def __init__(self, intervals):
		self.start = 0
		self.end = 0
		self.intervals = intervals
		self.merged = []
	
	def merge(self):
		self.intervals.sort(key=lambda x: x[0])
		print(self.intervals)
		for interval in intervals:
			self.start = interval[0]
			self.end = interval[1]
			if not self.merged or self.merged[-1][1] <= self.start:
				self.merged.append(interval)
			else:
				self.merged[-1][1] = max(self.end, self.merged[-1][1])
	
	def print_answer(self):
		print(self.merged)


if __name__ == "__main__":
	intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
	solution = Solution(intervals)
	solution.merge()
	solution.print_answer()
