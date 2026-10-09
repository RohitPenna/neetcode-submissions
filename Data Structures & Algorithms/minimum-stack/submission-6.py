class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minimum[-1]:
            self.minimum.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.minimum[-1]:
            self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1] if self.minimum[-1] != float('inf') else 0
