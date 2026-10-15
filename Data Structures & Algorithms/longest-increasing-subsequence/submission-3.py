class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * (len(nums))

        for i in range(len(nums)):
            for x in range(i):
                if nums[i] > nums[x]:
                    dp[i] = max(dp[i], dp[x] + 1)
        
        return max(dp)