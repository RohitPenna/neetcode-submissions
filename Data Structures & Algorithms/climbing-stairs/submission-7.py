class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n
        
        one = 1
        two = 2

        steps = 0
        for i in range(3, n+1):
            steps = one + two
            one = two
            two = steps
        
        return steps


        '''
        cache = {}

        def dfs(i):

            if i == n:
                return 1

            if i > n:
                return 0

            if i in cache:
                return cache[i]

            one = dfs(i + 1)
            two = dfs(i + 2)

            cache[i] = one + two

            return cache[i]

        return dfs(0)
        '''