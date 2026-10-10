class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse = True)

        stack = []

        for i in cars:

            time = (target - i[0]) / i[1]

            if stack:
                if stack[-1] < time:
                    stack.append(time)
            else:
                stack.append(time)
            
        return len(stack)

