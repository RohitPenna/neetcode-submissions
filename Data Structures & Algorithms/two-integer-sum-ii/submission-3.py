class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x = {}

        for i in range(len(numbers)):
            y = target - numbers[i]
            if y in x:
                return [x[y] + 1, i + 1]
            else:
                x[numbers[i]] = i