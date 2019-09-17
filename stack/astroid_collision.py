"""Astroid collision question"""
def astroid_collision(arr):
        stack = []
        for element in arr:
            if len(stack) == 0 or element > 0:
                stack.append(element)
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] == -element:
                        stack.pop()
                        break
                    elif stack[-1] < -element:
                        stack.pop()
                        continue
                    elif stack[-1] > -element:
                        break
                else:
                    stack.append(element)
                
        rev_stack = []
        while stack:
            rev_stack.append(stack.pop())
        result = []
        while rev_stack:
            result.append(rev_stack.pop())
        
        return result

if __name__ == "__main__":
    arr = [10, 2, -5]
    print(astroid_collision(arr))