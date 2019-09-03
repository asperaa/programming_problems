"""Prefix to postfix"""
def prefix_to_postfix(exp):
    stack = []
    operator = {"+": True, "-": True, "*": True, "/": True}
    for element in exp[::-1]:
        if element in operator:
            operand_1 = stack.pop()
            operand_2 = stack.pop()
            stack.append(operand_1+operand_2+element)
        else:
            stack.append(element)
    return stack.pop()

if __name__ == "__main__":
    exp_1 = "*+AB-CD"
    exp_2 = "*-A/BC-/AKL"
    print(prefix_to_postfix(exp_1))
    print(prefix_to_postfix(exp_2))
