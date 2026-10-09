class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:  # It's a closing bracket
                if stack:
                    top_element = stack.pop()
                else:
                    return False
                if mapping[char] != top_element:
                    return False
            else:  # It's an opening bracket
                stack.append(char)

        return not stack