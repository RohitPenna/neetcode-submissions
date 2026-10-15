from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        @cache
        def dfs(sum1, sum2, i):

            if i == len(nums):
                return sum1 == sum2
            
            return dfs(sum1 + nums[i], sum2, i+1) or dfs(sum1, sum2+ nums[i], i+1)
        
        if len(nums) == 1:
            return False
        
        return dfs(0, 0, 0)
