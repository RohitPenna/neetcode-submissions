class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)                  
        
        x = freq.most_common(k)

        y = [i[0] for i in x]

        return list(y)