class Solution:
    def countBits(self, n: int) -> List[int]:
        count = 1
        dp = [0] * (n+1)
        offset = 1
        power = 1

        while count <= n:
            if (2**power > n):
                for i in range(2**(power-1), n+1):
                    count +=1
                    dp[i] = 1 + dp[i-offset]
            else:
                for i in range(2**(power-1), 2**power):
                    count +=1
                    dp[i] = 1 + dp[i-offset]
            offset = 2**power
            power += 1

        return dp
