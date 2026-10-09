class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ran = set(nums)
        for i in range(len(nums)+1):
            if i not in ran:
                return i
        return 