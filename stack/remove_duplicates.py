"""Remove duplicates and maintain lexicographical sequence"""
def remove_dup(arr):
        stack = []
        seen = set()
        last_occurence = {element: i for i, element in enumerate(arr)}

        for i, element in enumerate(arr):
            if element not in seen:
                while stack and element < stack[-1] and i < last_occurence[stack[-1]]:
                    seen.discard(stack.pop())
                stack.append(element)
                seen.add(element)
        return "".join(stack)

if __name__ == "__main__":
    arr = "cbacdbc"
    print(remove_dup(arr))

        