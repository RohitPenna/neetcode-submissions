class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def bfs(left, right):
            count = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            return count

        tot = 0

        for i in range(len(s)):
            x = bfs(i, i)       # Odd palindrome
            y = bfs(i, i + 1)   # Even palindrome

            tot += x
            tot += y

        return tot