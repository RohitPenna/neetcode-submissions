class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            pivot = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = pivot + nums[left] + nums[right]

                if total == 0:
                    ans.append([pivot, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return ans