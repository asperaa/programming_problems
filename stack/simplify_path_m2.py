"""Simplify the absolute path of the UNIX system using python functions"""
def simplify_path(path):
    stack = []
    for element in path.split("/"):
        if element in {"", "."}:
            continue
        elif element == "..":
            if stack:
                stack.pop()
        else:
            stack.append(element)
    return "/" + "/".join(stack)

if __name__ == "__main__":
    path = "/abc/..."
    print(simplify_path(path))