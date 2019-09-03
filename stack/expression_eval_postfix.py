"""Evaluate the postfix expression"""
def evaluate_postfix(exp):
    stack = []
    operator = {
        "+": True,
        "-": True,
        "*": True,
        "/": True
    }
    for element in exp:
        if element not in operator:
            stack.append(int(element))
        else:
            right = stack.pop()
            left = stack.pop()
            if element == "+":
                stack.append(left + right)
            elif element == "-":
                stack.append(left - right)
            elif element == "*":
                stack.append(left * right)
            else:
                if left * right < 0 and left % right != 0:
                    stack.append(left // right + 1)
                else:
                    stack.append(left // right)
    return stack.pop()

if __name__ == "__main__":
    exp_1 = ["2", "1", "+", "3", "*"]
    exp_2 = ["4", "13", "5", "/", "+"]
    exp_3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    
    exp = [exp_1, exp_2, exp_3]
    for expression in exp:
        print(evaluate_postfix(expression))

            
