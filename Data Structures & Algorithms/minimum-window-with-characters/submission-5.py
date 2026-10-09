
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        comp = Counter(t)
        cur = defaultdict(int)

        left = 0
        ans = ""
        have = 0
        need = len(comp)

        for right in range(len(s)):
            
            cur[s[right]] += 1

            if s[right] in comp and cur[s[right]] == comp[s[right]]:
                have += 1

            while have == need:
                if not ans or right - left + 1 < len(ans):
                    ans = s[left:right + 1]

                cur[s[left]] -= 1

                if s[left] in comp and cur[s[left]] < comp[s[left]]:
                    have -= 1

                left += 1

        return ans
