from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        @cache
        def dfs(i, cur):

            if cur == target:
                return True

            if i == len(nums) or cur > target:
                return False

            take = dfs(i + 1, cur + nums[i])
            skip = dfs(i + 1, cur)

            return take or skip

        return dfs(0, 0)