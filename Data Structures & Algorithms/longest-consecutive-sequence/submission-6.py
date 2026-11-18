class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        mapp = set(nums)

        ans = 0

        for i in mapp:
            
            if i - 1 not in mapp:

                curr = 1
                while i + curr in mapp:
                    curr += 1
                
                ans = max(ans, curr)
        
        return ans

