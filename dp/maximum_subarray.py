"""Maximum subarray sum"""
def maximum_subarry(nums):
    if not nums:
        return 0
    max_so_far = float('-inf')
    curr_max_sum = 0

    for num in nums:
        if curr_max_sum + num > num:
            curr_max_sum += num
        else:
            curr_max_sum = num

        max_so_far = max(max_so_far, curr_max_sum)

    return max_so_far

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maximum_subarry(arr)) 
    
