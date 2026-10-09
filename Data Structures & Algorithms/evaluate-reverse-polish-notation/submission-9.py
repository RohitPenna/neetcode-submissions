class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in tokens:

            if i in ['+', '-', '*', '/']:
                if i == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a+b)
                elif i == '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b/a))
                elif i == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a*b)
                elif i == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b-a)
            else:
                stack.append(int(i))
            
        if len(stack) == 1:
            return stack[0]
        return