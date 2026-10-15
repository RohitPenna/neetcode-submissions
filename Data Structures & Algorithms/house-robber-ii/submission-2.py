class Solution:
    def rob(self, nums: List[int]) -> int:
        
        one = 0
        two = 0
        noend = 0

        if len(nums) == 1:
            return nums[0]

        for num in nums[:-1]:
            cur = max(two, one + num)

            one = two
            two = cur

        noend = two
        one = 0
        two = 0

        for num in nums[1:]:
            cur = max(two, one + num)

            one = two
            two = cur

        
        return max(two, noend)