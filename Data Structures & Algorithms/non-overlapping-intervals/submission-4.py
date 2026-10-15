class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[0])

        count = 0
        prevEnd = float('-inf')

        for start, end in intervals:
            if start < prevEnd:
                count += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end

        return count