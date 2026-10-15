from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # [3, 1, 1, 3, 4]

        @cache
        def dfs(i):

            if i >= len(nums):
                return 0
            
            skip = dfs(i+1)
            take = nums[i] + dfs(i + 2)

            return max(skip, take)
        
        return dfs(0)
