from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        @cache
        def dfs(i, prev):

            if i == len(nums):
                return 0

            skip = dfs(i + 1, prev)

            take = 0

            if nums[i] > prev:
                take = 1 + dfs(i + 1, nums[i])

            return max(skip, take)

        return dfs(0, float('-inf'))