"""Remove outer parentheses"""
def remove_parenthese(exp):
    flag = 0
    stack = []
    result = ""
    for element in exp:
        if element == "(":
            flag += 1
            if flag > 1:
                stack.append(element)
            
        else:
            flag -= 1
            if flag > 0:
                stack.append(element)
            
    while stack:
        result += stack.pop()
    
    return result[::-1]

if __name__ == "__main__":
    e1 = "(()())(())"
    e2 = "(()())(())(()(()))"
    e3 = "()()"
    expression_list = [e1, e2, e3]
    for e in expression_list:
        print(remove_parenthese(e))