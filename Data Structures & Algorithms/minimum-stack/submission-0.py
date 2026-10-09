class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # tracks min at each state

    def push(self, val):
        self.stack.append(val)
        # push the new min (either val or current min)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()  # keep in sync

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]