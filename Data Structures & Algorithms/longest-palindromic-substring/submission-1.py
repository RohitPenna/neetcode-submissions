class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def bfs(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1:right]

        cur = ""

        for i in range(len(s)):
            x = bfs(i, i)       # Odd palindrome
            y = bfs(i, i + 1)   # Even palindrome

            if len(x) > len(cur):
                cur = x

            if len(y) > len(cur):
                cur = y

        return cur