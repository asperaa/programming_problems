"""House robber. 1D DP. Time - O(n). Space - O(1)"""
def max_loot(nums):
    prev_max = 0
    curr_max = 0

    for num in nums:
        temp = curr_max
        curr_max = max(prev_max + num, curr_max)
        prev_max = temp
    
    return curr_max

if __name__ == "__main__":
    arr = [1, 2, 3, 1]
    print(max_loot(arr))