from functools import cache

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ans = nums[0]
        curMax = nums[0]
        curMin = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            a = num
            b = curMax * num
            c = curMin * num

            curMax = max(a, b, c)
            curMin = min(a, b, c)

            ans = max(ans, curMax)

        return ans
        
        '''
        dp = [1] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            
            if (nums[i] * dp[i - 1]) > dp[i - 1]:
                dp[i] = nums[i] * dp[i - 1]
            else:
                dp[i] = nums[i]
        
        return max(dp)

        '''