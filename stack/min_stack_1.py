class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        
        

    def push(self, x: int) -> None:
        if len(self.s1) == 0:
            self.s1.append(x)
            self.s2.append(x)
        else:
            self.s1.append(x)
            if x < self.s2[-1]:
                self.s2.append(x)
            else:
                self.s2.append(self.s2[-1])
        return None

    def pop(self) -> None:
        if len(self.s1) == 0:
            return None
        self.s1.pop()
        self.s2.pop()
        

    def top(self) -> int:
        if len(self.s1) == 0:
            return None
        return self.s1[-1]
        

    def getMin(self) -> int:
        if len(self.s1) == 0:
            return None
        return self.s2[-1]
            
        

if __name__ == "__main__":
    stack = MinStack()
    stack.push(1)
    stack.push(2)
    stack.push(-3)
    stack.push(4)
    print(stack.getMin())
