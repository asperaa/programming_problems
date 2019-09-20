"""Trapping rain water problem using stacks"""
def trapping_rain_water(height):
    stack = []
    length = len(height)
    current = 0
    water_trap = 0
    while current != length:
        while stack and height[stack[-1]] < height[current]:
            
            top = stack.pop()
            if not stack:
                break

            width = current - stack[-1] - 1
            height_length = min(height[current], height[stack[-1]]) - height[top]
            water_trap += width * height_length
        stack.append(current)
        current += 1
    return water_trap

if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trapping_rain_water(arr))
            




    