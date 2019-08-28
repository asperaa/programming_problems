"""Find the numbers of days until the next warmest temperature"""
def daily_temp(T):
    stack = []
    length = len(T)
    # initialise all the values from zero. Hepls in last index value.
    result = [0] * length
    for i in range(length - 1, -1, -1):     
        # pop until you find an element greater than the current element
        while stack and T[i] >= T[stack[-1]]:
            stack.pop()
        if stack:
            result[i] = stack[-1] - i
        # store the index values for latest greater element
        stack.append(i)
    return result
if __name__ == "__main__":
    arr = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
    print(daily_temp(arr))