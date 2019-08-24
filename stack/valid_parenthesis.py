"""Check whether the experession has balanced parenthesis"""
def is_valid(brackets):
    bracket_map = {'(':')', '[': ']', '{': '}'}
    stack = []
    flag = 0
    for bracket in brackets:
        if bracket in bracket_map.keys():
            stack.append(bracket)
        else:
            try:
                if bracket == bracket_map[stack[-1]]:
                    stack.pop()
                else:
                    flag = 1
                    break
            except:
                flag = 1
                break
    if len(stack) != 0 or flag == 1 :
        return False
    else:
        return True

if __name__ == "__main__":
    brackets = ["(])"]
    for bracket in brackets:
        print(is_valid(bracket))
