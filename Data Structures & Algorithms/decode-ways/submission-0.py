from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        
        # 1012
        #(10, 1, 2) (10, 12)

        #(1112)
        #(1, 11, 2) (11, 1, 2) (1, 1, 12)

        @cache
        def dfs(i):
            if i == len(s):
                return 1

            if s[i] == "0":
                return 0

            one = dfs(i + 1)

            two = 0
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                two = dfs(i + 2)

            return one + two

        return dfs(0)



