class Solution:
    def isValid(self, s: str) -> bool:
        
        maps = {
            '(':')',
            '{':'}',
            '[':']'
        }

        stack = []

        for i in s:
            if i in maps:
                stack.append(i)
            else:
                if stack:
                    x = stack.pop()
                    if i != maps[x]:
                        return False
                else:
                    return False
        
        return not stack