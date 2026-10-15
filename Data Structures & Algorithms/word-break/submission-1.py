from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def dfs(s):

            if s == "":
                return True
            
            for x in wordDict:
                if s.startswith(x):
                    rep = s[len(x):]

                    if dfs(rep):
                        return True

            return False
        
        return dfs(s)