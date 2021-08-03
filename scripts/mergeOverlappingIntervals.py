"""
You are given an array (list) of interval pairs as input where each interval has a start and end timestamp. 
The input array is sorted by starting timestamps. 
You are required to merge overlapping intervals and return a new output array.

"""

class Solution():
    def main(self, intervals):
        intervals.sort()
        result = []
        print(intervals)
        for idx in range(len(intervals)):
            print(idx, result)
            if not result:
                result.append(intervals[idx])
            elif intervals[idx][0] <= result[-1][1] and intervals[idx][0] >= result[-1][0]:
                result[-1][1] = max(intervals[idx][1], result[-1][1])
            else:
                result.append(intervals[idx])
        print(result)
        
        
        
if __name__ == "__main__":
    intervals = [[3, 7], [1, 5], [4, 6], [6, 8], [1, 12]]
    Solution().main(intervals)