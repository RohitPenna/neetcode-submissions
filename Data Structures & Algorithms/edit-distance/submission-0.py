from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @cache
        def dfs(i, j):

            if i == len(word1):
                return len(word2) - j

            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            ins = dfs(i, j + 1)
            rep = dfs(i + 1, j + 1)
            de = dfs(i + 1, j)

            return 1 + min(ins, rep, de)

        return dfs(0, 0)