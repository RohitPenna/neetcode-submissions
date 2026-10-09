class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        longest = 1
        count = 1

        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                continue

            elif nums[i + 1] - nums[i] == 1:
                count += 1

            else:
                longest = max(longest, count)
                count = 1

        longest = max(longest, count)

        return longest