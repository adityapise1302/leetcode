class MinStack:

    def __init__(self):
        self.s = []
        self.min = []

    def push(self, val: int) -> None:
        self.min.append(min(val, self.min[-1])) if len(self.min) != 0 else self.min.append(val)
        self.s.append(val)

    def pop(self) -> None:
        self.s.pop() if len(self.s) != 0 else None
        self.min.pop()

    def top(self) -> int:
        return self.s[-1] if len(self.s) != 0 else None

    def getMin(self) -> int:
        return self.min[-1] if len(self.min) != 0 else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()