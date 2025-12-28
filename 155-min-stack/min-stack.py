class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.min.append(val)
        else:
            if self.min[-1] >= val:
                self.min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        pop_val = self.stack.pop()
        if pop_val == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()