from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {0: 1}

        for num in nums:
            new_dp = defaultdict(int)

            for s, count in dp.items():
                new_dp[s + num] += count
                new_dp[s - num] += count

            dp = new_dp

        return dp.get(target, 0)

        
        '''
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
        '''
