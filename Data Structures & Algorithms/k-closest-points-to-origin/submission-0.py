from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = []
        heapq.heapify(dist)

        for i in points:
            x = i[0]
            y = i[1]

            calc = sqrt((x - 0)**2 + (y - 0)**2)

            heapq.heappush(dist, (-calc, x, y))

            if len(dist) > k:
                heapq.heappop(dist)

        ans = []
        
        for i in dist:
            ans.append([i[1], i[2]])
        
        return ans
        

        