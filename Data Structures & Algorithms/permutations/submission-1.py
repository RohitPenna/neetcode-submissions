class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        used = set()
        
        def dfs(cur):
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return
            
            for i in range(len(nums)):
                
                if nums[i] in used:
                    continue
                used.add(nums[i])
                cur.append(nums[i])
                dfs(cur)
                cur.pop()
                used.remove(nums[i])
        
        dfs([])
        return ans