class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def isP(s):
            left = 0
            right = len(s) - 1

            while left < right:
                l = s[left]
                r = s[right]
                
                if l != r:
                    return False

                left += 1
                right -= 1
            
            return True
        
        def dfs(cur, index):

            if index == len(s):
                ans.append(cur.copy())
                return
            
            for i in range(index, len(s)):
                if isP(s[index:i+1]):
                    cur.append(s[index:i+1])
                    dfs(cur, i + 1)
                    cur.pop()
        
        dfs([], 0)
        return ans


