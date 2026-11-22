class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        sums = {0:0, 1:0, 2:0}

        for num in nums:
            sums[num] += 1
        
        x = sums[1]
        sums[1] = sums[0]
        sums[2] = sums[1] + x

        for i in range(len(nums)):

            if i >= sums[2]:
                nums[i] = 2
            elif i >= sums[1]:
                nums[i] = 1
            else:
                nums[i] = 0
        
        