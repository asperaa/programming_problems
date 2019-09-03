"Backspace string compare"
def backspaceCompare(self, S: str, T: str) -> bool:
    stack_1 = []
    stack_2 = []
    
    for element in S:
        if element == "#":
            if stack_1:
                stack_1.pop()
            continue
        stack_1.append(element)
    
    for element in T:
        if element == "#":
            if stack_2:
                stack_2.pop()
            continue
        stack_2.append(element)
    
    while stack_1 and stack_2:
        pop_1 = stack_1.pop()
        pop_2 = stack_2.pop()
        if pop_1 != pop_2:
            return False
    if len(stack_1) == len(stack_2):
        return True
    else:
        return False