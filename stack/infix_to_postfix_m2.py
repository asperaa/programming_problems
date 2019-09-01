"""Convert an expression from infix to postfix"""
def infix_to_postfix(exp):
    stack = []
    result = ""
    precedence_order = {
        "^": 3,
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1,
        "(": 0
    }

    for element in exp:
        if element.isalpha():
            result += element
        elif element == "(":
            stack.append(element)
        elif element == ")":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.pop()
        else:
            if stack and precedence_order[element] > precedence_order[stack[-1]]:
                stack.append(element)
            else:
                while stack and precedence_order[element] <= precedence_order[stack[-1]]:
                    result += stack.pop()
                stack.append(element)
    while stack:
        result += stack.pop()
    return result  

if __name__ == "__main__":
    exp = "(A+B/C*(D+E)-F)"
    print(infix_to_postfix(exp))