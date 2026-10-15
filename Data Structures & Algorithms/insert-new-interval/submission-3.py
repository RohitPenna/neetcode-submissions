class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        i = 0

        # Skip intervals that come before newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i += 1

        start = i

        # Merge all overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Replace overlapping intervals with merged interval
        intervals[start:i] = [newInterval]

        return intervals