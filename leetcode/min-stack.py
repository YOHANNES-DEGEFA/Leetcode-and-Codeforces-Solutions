class MinStack:

    def __init__(self):
        self.stk = []
        self.min = float('inf')
       

    def push(self, val: int) -> None:
        self.min = min(self.min,val)
        self.stk.append(val)

    def pop(self) -> None:
        c = self.stk.pop()
        if c == self.min: 
            temp = self.stk[:]
            self.min = float('inf')
            while temp:
                self.min = min(self.min,temp.pop())
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()