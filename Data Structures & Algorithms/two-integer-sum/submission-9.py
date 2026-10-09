class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = set(nums)

        for i in nums:
            complement = target - i

            if complement in x:
                if complement == i:
                    first = nums.index(i)

                    try:
                        second = nums.index(i, first + 1)
                        return [first, second]
                    except ValueError:
                        continue

                return [nums.index(i), nums.index(complement)]