class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        rep = set(nums)
        count = 0

        for i in range(len(nums)):
            if (nums[i]-1) in rep:
                continue
            val = nums[i]
            x = True
            y = 1
            while x:
                if (val+1) in rep:
                    y += 1
                else:
                    x = False
                val += 1
            if y > count:
                count = y
        return count

        