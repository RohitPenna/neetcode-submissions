class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        jumps = 0
        
        for i in range(len(nums)):
            
            jumps = max(nums[i], jumps)

            if jumps == 0 and i != len(nums) - 1:
                return False
            
            jumps -= 1
        
        return True