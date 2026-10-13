class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        visited = set()
        ans = []

        def dfs(index, cur):

            if tuple(cur) not in visited:
                visited.add(tuple(cur))
                ans.append(cur.copy())
            else:
                return
            
            if len(cur) == len(nums):
                return
            
            for i in range(index, len(nums)):
                cur.append(nums[i])
                dfs(i + 1, cur)
                cur.pop()
        
        dfs(0, [])
        return ans