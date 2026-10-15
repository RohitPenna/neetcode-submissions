class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = float('-inf')

        curSum = nums[0]
        
        for i in range(1, len(nums)):
            
            x = nums[i]
            ans = max(ans, curSum)

            if curSum + x < x:
                curSum = x
            else:
                curSum += x

        return max(ans, curSum)