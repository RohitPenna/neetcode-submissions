class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num = prices[0]
        maxDif = 0
        dif = 0
        for i in prices:
            if i > num:
                dif = i - num
            else:
                num = i
            if dif > maxDif:
                maxDif = dif
        return maxDif


        