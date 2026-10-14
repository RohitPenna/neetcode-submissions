import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def calc(speed):

            count = 0
            for i in piles:
                count += math.ceil(i/speed)
            
            return count

        left = 1
        right = max(piles)

        while left < right:

            mid = (left + right) // 2

            count = calc(mid)

            if count > h:
                left = mid + 1
            else:
                right = mid
        
        return left
        
        