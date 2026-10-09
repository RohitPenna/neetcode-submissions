class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = {}

        for i in strs:
            x = "".join(sorted(i))
            if x in dic:
                dic[x].append(i)
            else:
                dic[x] = [i]
        
        res = []

        for i in dic:
            res.append(dic[i])
        return res