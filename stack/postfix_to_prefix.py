"""Postfix to prefix"""
def postfix_to_prefix(exp):
    stack = []
    operator = {"+": True, "-": True, "*": True, "/": True}
    for element in exp:
        if element in operator:
            operand_1 = stack.pop()
            operand_2 = stack.pop()
            stack.append(element+operand_2+operand_1)
        else:
            stack.append(element)
    return stack.pop() 

if __name__ == "__main__":
    exp_1 = "AB+CD-*"
    exp_2 = "ABC/-AK/L-*"
    print(postfix_to_prefix(exp_1))
    print(postfix_to_prefix(exp_2))