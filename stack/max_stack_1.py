"""Implement max stack"""
class MaxStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def is_empty(self):
        return len(self.s1) == 0

    def push(self, val):
        
        if self.is_empty():
            self.s1.append(val)
            self.s2.append(val)
            return None
        
        self.s1.append(val)
        if val > self.s2[-1]:
            self.s2.append(val)
        else:
            self.s2.append(self.s2[-1])
        return None
    
    def pop(self):
        
        if self.is_empty():
            return None
        self.s1.pop()
        self.s2.pop()
        return
    
    def getMax(self):
        if self.is_empty():
            return None
        return self.s2[-1]
    
    def top(self):
        if self.is_empty():
            return None
        return self.s1[-1]
            
if __name__ == "__main__":
    stack = MaxStack()
    stack.push(1)
    stack.push(200)
    stack.push(3)
    stack.push(400)
    print(stack.getMax())
    stack.pop()
    print(stack.getMax())

    