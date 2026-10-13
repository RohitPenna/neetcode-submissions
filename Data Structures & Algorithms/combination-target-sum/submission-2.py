class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def dfs(index, cur, tot):

            if tot == target:
                ans.append(cur.copy())
            
            if tot > target or index == len(nums):
                return
            
            for i in range(index, len(nums)):
                cur.append(nums[i])
                dfs(i, cur, tot + nums[i])
                cur.pop()
        
        dfs(0, [], 0)
        return ans