class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def dfs(cur, i, tot):

            if tot > target:
                return
            
            if tot == target:
                ans.append(cur.copy())
                return
            
            for x in range(i, len(nums)):
                cur.append(nums[x])
                dfs(cur, x, tot + nums[x])
                cur.pop()
        
        dfs([], 0, 0)
        return ans