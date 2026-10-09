from collections import Counter
from heapq import nlargest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)                  
        heap = []                             

        for val, count in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, val))
            else:
                if count > heap[0][0]:
                    heapq.heapreplace(heap, (count, val))
        return [val for _, val in heap]