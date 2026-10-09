class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}

        vals = [0] * (k)
        for i in range(len(nums)):
            if nums[i] in myDict.keys():
                myDict[nums[i]] += 1
            else:
                myDict[nums[i]] = 1
        
        top_keys = sorted(myDict, key=myDict.get, reverse=True)[:k]
        return list(top_keys)
