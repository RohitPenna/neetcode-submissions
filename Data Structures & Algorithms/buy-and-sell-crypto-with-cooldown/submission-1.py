from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @cache
        def dfs(i, holding):
            if i >= len(prices):
                return 0

            if holding:
                sell = prices[i] + dfs(i + 2, False)
                skip = dfs(i + 1, True)
                return max(sell, skip)

            else:
                buy = -prices[i] + dfs(i + 1, True)
                skip = dfs(i + 1, False)
                return max(buy, skip)

        return dfs(0, False)