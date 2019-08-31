"""Simplify the given absolute linux path to a file or folder"""
def simplify_path(path):
    stack = []
    i = 0
    result = "/"
    length = len(path)
    while i < length:
        temp_path_name = ""
        while i < length and path[i] == "/":
            i += 1
        while i < length and path[i] != "/":
            temp_path_name += path[i]
            i += 1
        if temp_path_name == ".":
            continue
        elif temp_path_name == "..":
            if stack:
                stack.pop()
        elif len(temp_path_name):
            stack.append(temp_path_name)
        i += 1

    rev_stack = []
    while stack:
        rev_stack.append(stack.pop())
    while rev_stack:

        if len(rev_stack) != 1:
            result += rev_stack.pop() + "/"
        else:
            result += rev_stack.pop()
    return result

if __name__ == "__main__":
    p1 = "/a//b////c/d//././/.."
    p2 = "/a/../../b/../c//.//"
    p3 = "/../"
    p4 = "/..."
    input_arr = [p1, p2, p3, p4]
    for i in input_arr:
        print(simplify_path(i))


