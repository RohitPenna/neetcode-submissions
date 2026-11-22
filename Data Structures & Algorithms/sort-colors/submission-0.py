class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(1, len(nums)):

            if nums[i] < nums[i-1]:
                x = i - 1
                place = nums[i]
                nums[i] = nums[i-1]
                nums[i-1] = place

                while x > 0:
                    if nums[x] < nums[x-1]:
                        place = nums[x]
                        nums[x] = nums[x-1]
                        nums[x-1] = place
                        x -= 1
                    else:
                        break
        