from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # [3, 1, 1, 3, 4]
        
        cache = {}

        def dfs(i):

            if i >= len(nums):
                return 0

            if i in cache:
                return cache[i]
            
            skip = dfs(i+1)
            take = nums[i] + dfs(i + 2)

            cache[i] = max(skip, take)
            return cache[i]
        
        return dfs(0)
        '''

        one = 0
        two = 0

        for num in nums:
            cur = max(two, one + num)

            one = two
            two = cur

        return two
        '''
