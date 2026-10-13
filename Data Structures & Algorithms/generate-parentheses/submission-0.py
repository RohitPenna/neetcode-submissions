class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []

        def dfs (s, op, cl):

            if op == cl and op == n:
                ans.append(s)
                return

            if op < n:
                s += "("
                dfs(s, op + 1, cl)
                s = s[:-1]
            if cl < op:
                s += ")"
                dfs(s, op, cl + 1)
                s = s[:-1]
            
            return
        
        dfs("", 0, 0)
        return ans
