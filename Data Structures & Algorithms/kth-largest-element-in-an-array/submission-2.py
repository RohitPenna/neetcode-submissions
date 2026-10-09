import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        ans = nums

        heapq.heapify(ans)

        while len(ans) > k:
            heapq.heappop(ans)

        return ans[0]