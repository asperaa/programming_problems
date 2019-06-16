# class for conversion
class Conversion:

    # function to initiate various variables
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.array = []
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    # function to check whether stack is empty
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    # function to show the top of stack
    def peek(self):
        if self.is_empty():
            print("Empty stack")
            return -1
        
        return self.array[-1]
    
    # function to adda new_element to the stack
    def push(self, data):
        if self.top == self.capacity - 1:
            print("Stack overflow")
            return -1
        self.top += 1
        self.array.append(data)
    
    # function to pop the top of stack
    def pop(self):
        if self.is_empty():
            print("Empty stack")
            return -1
        self.top -= 1
        return self.array.pop()
    
    # function to check whether the char is operand or not
    def is_operand(self, ch):
        return ch.isalpha()

    # function to check whether char's precedence is strictly 
    # less than the top of stack char
    def is_not_greater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
    

    # function for actual conversion of infix to postfix
    def infix_to_postfix(self, exp):

        for i in exp:
            # if character of the exp is an operand, then it goes to the output
            if self.is_operand(i):
                # print(i, i.isalpha())
                # print(self.output)
                self.output.append(i)
            # if the character of the exp is open bracket, then it goes to the stack
            elif i == '(':
                self.push(i)
            # if the char is a close bracket, then pop from stack until it is empty
            # or it reaches the bottom of the stack
            elif i == ')':
                while((not self.is_empty()) and self.peek() != '('):
                    self.output.append(self.pop())
                if (not self.is_empty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
            # case of handling an operator
            else:
                while((not self.is_empty()) and self.is_not_greater(i)):
                    self.output.append(self.pop())
                self.push(i)
            
            # pop all the remaining operator from the stack
        while not self.is_empty():
            self.output.append(self.pop())
            # print(self.output)
        print("".join(self.output))

if __name__ == "__main__":
    exp = "a+b*(c^d-e)^(f+g*h)-i"
    c = Conversion(len(exp))
    c.infix_to_postfix(exp)
            
            
            