"""Trapping rain water -- two pointers"""
def trap_water(height):
        if not height:
            return 0
        length = len(height)
        ans = 0
        left = 0
        right = length - 1
        left_max = height[0]
        right_max = height[length -1]
        while left < right:
            if left_max < height[left]:
                left_max = height[left]
            if right_max < height[right]:
                right_max = height[right]
            if left_max < right_max:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1

        return ans

if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap_water(height))