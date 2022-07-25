class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        # print(self.stack)
        # for i in range(len(self.stack)-1, -0, -1):
        #     self.stack[i] = self.stack[i-1]
        # self.stack[0] = x
            


    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            print(self.stack2)
        return self.stack2.pop()


    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            print(self.stack2)
        return self.stack2[-1]


    def empty(self) -> bool:
        while not self.stack1 and not self.stack2:
            return True
        return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()