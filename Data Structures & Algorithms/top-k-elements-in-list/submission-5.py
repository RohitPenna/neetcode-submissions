from collections import Counter
from heapq import nlargest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)                  
        
        x = freq.most_common()

        res = []

        counter = 0
        for i, num in x:
            res.append(i)
            counter += 1
            if counter == k:
                return res

        return res