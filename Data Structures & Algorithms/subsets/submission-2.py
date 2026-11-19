class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def dfs(cur, i):
            
            ans.append(cur.copy())

            for x in range(i, len(nums)):

                cur.append(nums[x])
                dfs(cur, x + 1)
                cur.pop()

            return
        
        dfs([], 0)
        return ans