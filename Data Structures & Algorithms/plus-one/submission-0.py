class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits) - 1, -1, -1):

            x = digits[i] + 1
            if x == 10:
                digits[i] = 0
            else:
                digits[i] = x
                return digits
    
        digits[0] = 1
        digits.append(0)
        return digits