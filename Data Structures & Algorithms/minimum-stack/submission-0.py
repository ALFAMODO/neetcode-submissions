class MinStack:

    def __init__(self):
        self.stack=[]
        self.ms=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.ms or val <= self.ms[-1]:
            self.ms.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.ms[-1]:
            self.ms.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.ms[-1]
        
