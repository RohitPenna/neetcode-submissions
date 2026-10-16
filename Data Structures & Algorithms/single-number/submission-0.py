class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        x = nums[0]

        for i in nums[1:]:
            x = x ^ i
        
        return x