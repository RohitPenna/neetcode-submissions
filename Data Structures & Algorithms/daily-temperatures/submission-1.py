class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            val = temperatures[i]

            while stack and val > stack[-1][0]:
                x = stack.pop()

                ans[x[1]] = i - x[1]
            
            stack.append((val, i))

        return ans
