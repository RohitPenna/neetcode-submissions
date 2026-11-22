from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        x = len(nums) // 3

        index = Counter(nums)
        ans = []

        for i in index:
            if index[i] > x:
                ans.append(i)
        
        return ans