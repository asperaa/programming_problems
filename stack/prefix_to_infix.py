"""Prefix to infix"""
def prefix_to_infix(exp):
    stack = []
    operator = {"+": True, "-": True, "*": True, "/": True}
    for element in exp[::-1]:
        temp_var_1 = ""
        temp_var_2 = ""
        if element in operator:
            temp_var_1 = stack.pop()
            temp_var_2 = stack.pop()
            stack.append("(" + temp_var_1 + element + temp_var_2 + ")")
        else:
            stack.append(element)
    return stack.pop()

if __name__ == "__main__":
    exp_1 = "*+AB-CD"
    exp_2 = "*-A/BC-/AKL"
    print(prefix_to_infix(exp_1))
    print(prefix_to_infix(exp_2))
