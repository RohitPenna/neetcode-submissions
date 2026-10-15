class Solution:
    def climbStairs(self, n: int) -> int:
        
        '''
        # n = 5
        # 11111, 1112, 1121, 1211, 2111, 221, 212

        dp = [0] * (n + 1)
        dp[1] = 1
        if n >= 2:
            dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i -2]
        
        return dp[n]
        '''

        if n == 1:
            return 1
        if n == 2:
            return 2

        one = 1
        two = 2
        cur = 0

        for i in range(3, n + 1):
            cur = one + two
            one = two
            two = cur
        
        return cur