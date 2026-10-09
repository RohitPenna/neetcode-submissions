class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        dups = defaultdict(int)

        maxfreq = 0
        left = 0
        tot = 0

        for r in range(len(s)):
            dups[s[r]] += 1

            maxfreq = max(maxfreq, dups[s[r]])

            while (r - left + 1) - maxfreq > k:
                dups[s[left]] -= 1
                left += 1
            
            tot = max(tot, r-left+1)

        return tot