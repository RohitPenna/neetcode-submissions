from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def dfs(i, s):
            if i == len(nums) and s == target:
                return 1
            if i == len(nums):
                return 0
            
            add = dfs(i + 1, s + nums[i])
            sub = dfs(i + 1, s-nums[i])

            return add + sub
        
        return dfs(0, 0)
