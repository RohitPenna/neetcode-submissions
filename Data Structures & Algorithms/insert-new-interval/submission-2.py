class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for i in range(len(intervals)):

            x = intervals[i]

            # Current interval is before newInterval
            if x[1] < newInterval[0]:
                res.append(x)

            # Current interval is after newInterval
            elif x[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]

            # Overlapping intervals
            else:
                newInterval[0] = min(newInterval[0], x[0])
                newInterval[1] = max(newInterval[1], x[1])

        res.append(newInterval)

        return res