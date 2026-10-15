from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        x = Counter(s)
        ans = []
        contains = set()

        count = 0

        for i in range(len(s)):
            count += 1
            val = s[i]
            contains.add(val)
            x[val] -= 1
            if x[val] == 0:
                contains.remove(val)
            if not contains:
                ans.append(count)
                count = 0
        
        return ans

