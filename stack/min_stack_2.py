"""Minstack in constant linear time"""

class MinStack:
    def __init__(self):
        self.s1 = []
        self.minn = 0
    
    def push(self, val):
        if len(self.s1) == 0:
            self.s1.append(val)
            self.min = val
            return None
        if val < self.minn:
            hide_val = 2*val - self.minn
            self.s1.append(hide_val)
            self.minn = val
        else:
            self.s1.append(val)
        return None

    def pop(self):
        if len(self.s1) == 0:
            print("Empty stack")
            return None    
        popped_val = self.s1.pop()
        if popped_val < self.minn:
            self.minn = 2*self.minn - popped_val
        return None
    
    def get_min(self):
        if len(self.s1) == 0:
            return None
        return self.minn
    
    def is_empty(self):
        return len(self.s1) == 0

    def top(self):
        if self.is_empty():
            return

        return self.s1[-1]

if __name__ == "__main__":
    stack = MinStack()
    
    stack.push(1)
    stack.push(2)
    stack.push(-100)
    stack.push(0)
    stack.push(-200)
    stack.push(100)
    stack.pop()
    stack.pop()
    print(stack.get_min())

        