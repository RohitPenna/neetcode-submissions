class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        ans = nums[0]
        curSum = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            curSum = max(x, curSum + x)
            ans = max(ans, curSum)

        return ans