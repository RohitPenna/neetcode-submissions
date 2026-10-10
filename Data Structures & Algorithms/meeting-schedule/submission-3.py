"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        heap = []
        
        for i in intervals:
            heap.append([i.start, i.end])
        
        heap.sort()

        for i in range(len(heap) - 1):
            if heap[i][1] > heap[i+1][0]:
                return False
        return True
