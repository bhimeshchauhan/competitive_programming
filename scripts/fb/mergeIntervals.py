class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            if not merged or merged[-1][1] < start:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], end)
        return merged
	