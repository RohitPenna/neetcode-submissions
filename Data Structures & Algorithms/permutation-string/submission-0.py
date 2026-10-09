
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        comp = Counter(s1)

        left = 0
        right = len(s1) - 1

        cur = Counter(s2[left:right])

        while right < len(s2):

            cur[s2[right]] += 1

            if cur == comp:
                return True

            cur[s2[left]] -= 1

            if cur[s2[left]] == 0:
                del cur[s2[left]]

            left += 1
            right += 1

        return False
