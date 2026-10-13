class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()

        def dfs(index, cur):

            ans.append(cur.copy())
            
            for i in range(index, len(nums)):

                if i > index and nums[i] == nums[i - 1]:
                    continue

                cur.append(nums[i])
                dfs(i + 1, cur)
                cur.pop()
        
        dfs(0, [])
        return ans