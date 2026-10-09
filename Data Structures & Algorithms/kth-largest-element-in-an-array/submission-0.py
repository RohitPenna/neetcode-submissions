import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        ans = [-x for x in nums]

        heapq.heapify(ans)

        x = 0
        for i in range(k):
            x = -heapq.heappop(ans)

        return x