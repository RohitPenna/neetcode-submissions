class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        dup = set()
        dup.add(s[0])

        left = 0
        right = 1
        longest = 0

        while right < len(s):

            if s[right] in dup:

                longest = max(longest, len(dup))

                while s[right] in dup:
                    dup.remove(s[left])
                    left += 1
                dup.add(s[right])
                right += 1
            else:
                dup.add(s[right])
                right += 1
        
        return max(longest, len(dup))
