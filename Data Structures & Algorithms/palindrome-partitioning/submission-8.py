from functools import cache

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        @cache
        def isP(left, right):
            if left >= right:
                return True

            if s[left] != s[right]:
                return False

            return isP(left + 1, right - 1)
        
        def dfs(cur, index):

            if index == len(s):
                ans.append(cur.copy())
                return
            
            for i in range(index, len(s)):
                if isP(index, i):
                    cur.append(s[index:i+1])
                    dfs(cur, i + 1)
                    cur.pop()
        
        dfs([], 0)
        return ans


