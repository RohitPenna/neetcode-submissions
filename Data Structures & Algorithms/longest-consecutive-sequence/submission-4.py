class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seq = 0

        n = set(nums)

        for i in range(len(nums)):

            count = 1

            if nums[i] + 1 not in n:

                while nums[i] - count in n:
                    count += 1
                
                seq = max(seq, count)
            
        return seq
