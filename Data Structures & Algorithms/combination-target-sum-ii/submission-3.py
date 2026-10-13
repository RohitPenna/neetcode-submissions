class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(index, cur, tot):
            
            if tot == target:
                ans.append(cur.copy())
                return
            
            if tot > target:
                return
            
            for i in range(index, len(candidates)):
                
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                cur.append(candidates[i])
                dfs(i + 1, cur, tot + candidates[i])
                cur.pop()
        
        dfs(0, [], 0)
        return ans