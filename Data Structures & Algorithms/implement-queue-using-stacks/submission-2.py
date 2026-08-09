class MyQueue:

    def __init__(self):
        self.stack=[]
        self.s=[]

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.s:
            while self.stack:
                value=self.stack.pop()
                self.s.append(value)
        return self.s.pop()

    def peek(self) -> int:
        if not self.s:
            while self.stack:
                self.s.append(self.stack.pop())
        return self.s[-1]

    def empty(self) -> bool:
        return True if not self.stack and not self.s else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()