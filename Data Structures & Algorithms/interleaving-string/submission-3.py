from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        @cache
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True

            x = i + j

            if i < len(s1) and s3[x] == s1[i]:
                if dfs(i + 1, j):
                    return True

            if j < len(s2) and s3[x] == s2[j]:
                if dfs(i, j + 1):
                    return True

            return False

        if len(s1) + len(s2) != len(s3):
            return False

        return dfs(0, 0)