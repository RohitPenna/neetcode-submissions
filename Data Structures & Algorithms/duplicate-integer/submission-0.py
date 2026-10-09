class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        takern = set()
        for i in nums:
            if i in takern:
                return True
            takern.add(i)
        return False
