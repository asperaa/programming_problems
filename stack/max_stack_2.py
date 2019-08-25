class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        
    def is_empty(self):
        return len(self.s1) == 0
        
    def push(self, val: int) -> None:
        if self.is_empty():
            self.s1.append(val)
            self.s2.append(val)
            return None
        self.s1.append(val)
        if val > self.s2[-1]:
            self.s2.append(val)
        else:
            self.s2.append(self.s2[-1])
        return

    def pop(self) -> int:
        self.s2.pop()
        return self.s1.pop()
        

    def top(self) -> int:
        return self.s1[-1]

    def peekMax(self) -> int:
        return self.s2[-1]
        

    def popMax(self) -> int:
        max_element = self.peekMax()
        temp_stack = []
        # print(self.s1[-1])
        while self.s1[-1] != max_element:
            self.s2.pop()
            temp_stack.append(self.s1.pop())
        # print(self.s1, self.s2)
        self.s1.pop()
        self.s2.pop()
        # print(temp_stack)
        for _ in range(len(temp_stack)):
            self.s1.append(temp_stack.pop())
            if self.s2 == []:
                self.s2.append(self.s1[-1])
            else:
                if self.s1[-1]> self.s2[-1]:
                    self.s2.append(self.s1[-1])
                else:
                    self.s2.append(self.s2[-1])
        return max_element
            
        
        

if __name__ == "__main__":
    stack = MaxStack()
    stack.push(5)
    stack.push(1)
    stack.push(6)
    print(stack.popMax())
    print(stack.popMax())
    