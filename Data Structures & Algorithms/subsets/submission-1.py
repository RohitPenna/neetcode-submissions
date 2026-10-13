class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        visited = set()
        ans = []

        def dfs(index, cur):

            ans.append(cur.copy())
            
            for i in range(index, len(nums)):
                cur.append(nums[i])
                dfs(i + 1, cur)
                cur.pop()
        
        dfs(0, [])
        return ans