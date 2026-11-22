class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans = 0
        cursum = 0

        ps = {0:1}

        for x in nums:

            cursum += x

            ans += ps.get(cursum-k, 0)
            if cursum in ps:
                ps[cursum] += 1
            else:
                ps[cursum] = 1
        
        return ans
