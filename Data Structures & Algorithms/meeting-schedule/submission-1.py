"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        time = set()
        for i in intervals:
            if i.start in time or i.end in time:
                return False
            else:
                for x in range(i.start, i.end):
                    time.add(x)
        return True
