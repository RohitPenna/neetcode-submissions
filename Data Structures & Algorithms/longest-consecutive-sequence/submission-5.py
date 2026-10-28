class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seq = 0

        n = set(nums)

        for num in n:

            count = 1

            if num + 1 not in n:

                while num - count in n:
                    count += 1
                
                seq = max(seq, count)
            
        return seq
