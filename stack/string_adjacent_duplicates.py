"""Given a string S of lowercase letters, a duplicate removal 
consists of choosing two adjacent and equal letters, and removing them."""
def removeDuplicates(self, S: str) -> str:
    stack = []
    result = ""
    for element in S[::-1]:    
        if stack and element == stack[-1]:
            stack.pop()
        else:
            stack.append(element)
    while stack:
        result += stack.pop()
    return result

if __name__ = "__main__":
    string = "accaca"
    print(removeDuplicates(string))