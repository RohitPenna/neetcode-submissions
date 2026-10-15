class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                # Multiply individual digits
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                product = digit1 * digit2

                # Add previous value at this position
                total = product + res[i + j + 1]

                # Store ones digit
                res[i + j + 1] = total % 10

                # Carry remaining digits
                res[i + j] += total // 10

        # Remove leading zeros
        result = ''.join(map(str, res)).lstrip('0')

        return result