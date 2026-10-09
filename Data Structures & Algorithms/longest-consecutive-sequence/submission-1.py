class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        rep = set(nums)
        longest = 0

        for num in rep:
            if (num - 1) not in rep:
                current = num
                streak = 1

                while (current + 1) in rep:
                    current += 1
                    streak += 1

                longest = max(longest, streak)

        return longest