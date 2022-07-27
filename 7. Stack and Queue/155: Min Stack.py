class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = float('inf')


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minval = min(val, self.minval)

    def pop(self) -> None:
        if self.stack:
           temp = self.stack.pop()
        if temp == self.minval and self.stack:
            self.minval = min(self.stack)
        elif temp == self.minval:
            self.minval = float('inf')
            return temp        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stack:
            return self.minval



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()