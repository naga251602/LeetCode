class MyStack:
    def __init__(self):
        self.q = []
        self.front = 0
        self.rear = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.rear += 1

    def pop(self) -> int:
        self.rear -= 1
        return self.q.pop()
        
    def top(self) -> int:
        return self.q[self.rear-1]

    def empty(self) -> bool:
        return self.front == self.rear
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()