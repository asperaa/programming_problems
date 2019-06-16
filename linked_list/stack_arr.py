# function to create a stack
def create_stack():
    stack = []
    return stack

# function to check if the stack is empty
def is_empty(stack):
    return len(stack) == 0

# function to push
def push(stack, num):
    stack.append(num)
    print(num+" pushed into the stack")

# function to pop the item
def pop(stack):
    if is_empty(stack):
        print("Empty stack")
        return
    return stack.pop()


stack = create_stack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(90))
print(pop(stack) + " popped fron the stack")