class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = 0
        max_freq = 0
        best = 0

        for r, ch in enumerate(s):
            freq[ch] += 1
            max_freq = max(max_freq, freq[ch])

            # If replacements needed exceed k, shrink from the left
            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1)

        return best