class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dups = set()

        left = 0
        right = 1

        if not s:
            return 0
        
        dups.add(s[0])
        length = len(dups)
        
        while right < len(s):
            if s[right] not in dups:
                dups.add(s[right])
                right += 1
                continue
            
            length = max(length, len(dups))
            while s[right] in dups:
                dups.remove(s[left])
                left += 1
            dups.add(s[right])
            right += 1

        return max(length, len(dups))
