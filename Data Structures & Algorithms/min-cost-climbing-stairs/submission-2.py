class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        '''
        if len(cost) <= 2:
            return min(cost)
        
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 2] + cost[i-2], dp[i-1] + cost[i - 1])
        
        return dp[len(cost)]
        '''

        one = 0
        two = 0

        for i in range(2, len(cost) + 1):
            cur = min(one + cost[i - 2],
                      two + cost[i - 1])

            one = two
            two = cur

        return two