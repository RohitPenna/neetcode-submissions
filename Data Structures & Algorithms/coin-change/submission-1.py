from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}
        def dfs(remaining):
            if remaining == 0:
                return 0
            
            if remaining in cache:
                return cache[remaining]

            result = float('inf')

            for coin in coins:
                if coin <= remaining:
                    result = min(result, 1 + dfs(remaining - coin))

            cache[remaining] = result
            return result

        result = dfs(amount)

        return result if result != float('inf') else -1