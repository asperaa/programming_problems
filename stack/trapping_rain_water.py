"""Trapping rain water: DP Solution"""
def trapping_rain_water(heights):
    length = len(heights)
    left = [None] * length
    right = [None] * length
    left[0] = heights[0]
    right[length - 1] = heights[length - 1]
    
    for i in range(1, length):
        left[i] = max(left[i-1], heights[i])
    
    for i in range(length - 2, -1, -1):
        right[i] = max(right[i + 1], heights[i])
    
    water_units = 0
    for i in range(length):
        water_units += min(left[i], right[i]) - heights[i]
    
    return water_units

if __name__ == "__main__":
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trapping_rain_water(heights))
