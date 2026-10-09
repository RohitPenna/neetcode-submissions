class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero = 0

        for i in nums:
            if i == 0:
                zero += 1
                continue
            total = total * i

        if zero > 1:
            return [0] * len(nums)

        res = []

        for i in nums:
            if i == 0:
                res.append(total)
            elif zero == 1:
                res.append(0)
            else:
                res.append(total // i)

        return res