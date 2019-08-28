def is_digit(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

def calPoints(ops) -> int:
    stack = []
    total_sum = 0
    for i in ops:
        temp_sum = 0
        if is_digit(i):
            temp_sum = i
            total_sum += int(temp_sum)
            stack.append(int(i))
        elif i == 'C':
            popped = stack.pop()
            temp_sum = popped
            total_sum -= int(temp_sum)
        elif i == 'D':
            top = stack[-1]
            temp_sum = 2 * top
            total_sum += temp_sum
            stack.append(int(temp_sum))
        else:
            top_1 = stack.pop()
            top_2 = stack.pop()
            temp_sum = top_1 + top_2
            total_sum += temp_sum
            stack.append(top_2)
            stack.append(top_1)
            stack.append(int(temp_sum))
        print(temp_sum)
    return total_sum

if __name__ == "__main__":
    i = "-1"
    print(i.isdigit())
    a1 = ["5", "2", "C", "D", "+"]
    a2 = ["5","-2","4","C","D","9","+","+"]
    print(calPoints(a2))
