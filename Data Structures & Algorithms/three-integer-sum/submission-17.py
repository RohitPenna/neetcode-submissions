class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for pivot in range(len(nums) - 2):

            if pivot > 0 and nums[pivot] == nums[pivot - 1]:
                continue

            target = nums[pivot]
            left = pivot + 1
            right = len(nums) - 1

            while left < right:

                tot = target + nums[left] + nums[right]

                if tot == 0:
                    ans.append([target, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif tot > 0:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                else:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return ans