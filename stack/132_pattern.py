"""Detect the 132 pattern in an array"""

def pattern_132(arr):
    stack = []
    # make the third num large -ve to handle first iteration
    third_num = -float('inf')
    # start the prcoess from reverse
    for num in arr[::-1]:
        # check whether the third first num is smaller 
        # than the third num
        if third_num > num:
            return True
        # search for thr large num so far in reverse
        while stack and num > stack[-1]:
            third_num = stack.pop()
        stack.append(num)
    return False

if __name__ == "__main__":
    a1 = [3, 1, 4, 2]
    a2 = [2, 5, 4, 7, 8]
    a3 = [1, 2, 3, 4]
    a4 = [-1, 3, 2, 0]
    print(pattern_132(a1))
    print(pattern_132(a2))
    print(pattern_132(a3))
    print(pattern_132(a4))
