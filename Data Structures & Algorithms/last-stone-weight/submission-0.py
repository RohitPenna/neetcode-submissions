import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        ans = [-x for x in stones]

        heapq.heapify(ans)

        while len(ans) > 1:
            x = -heapq.heappop(ans)
            y = -heapq.heappop(ans)

            dif = abs(x-y)

            heapq.heappush(ans, -dif)

        return -ans[0]