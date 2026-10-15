class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def bfs(left, right):

            if left < 0 or right >= len(s):
                return 0

            if s[left] == s[right]:
                return 1 + bfs(left - 1, right + 1)

            return 0

        tot = 0

        for i in range(len(s)):
            x = bfs(i, i)       # Odd palindrome
            y = bfs(i, i + 1)   # Even palindrome

            tot += x
            tot += y
        return tot