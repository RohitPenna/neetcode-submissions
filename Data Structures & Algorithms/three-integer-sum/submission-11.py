class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()

        nums = sorted(nums)
        print(nums)

        for i in range(len(nums)):
            pivot = nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:
                
                l = nums[left]
                r = nums[right]

                total = l + r + pivot

                if total == 0:
                    ans.add(tuple(sorted([l, pivot, r])))
                    left +=1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        
        answer = [list(triplet) for triplet in ans]
        return answer