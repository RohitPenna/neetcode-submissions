class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = [["" for _ in range(len(strs))] for _ in range(len(strs))]

        maap = defaultdict(list)

        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            maap[key].append(strs[i])

        return list(maap.values())