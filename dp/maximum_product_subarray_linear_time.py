"""Maximum product subarray. Linear time"""
def max_pro(nums):
    if not nums:
        return 0
    length = len(nums)
    maxx = nums[0]
    minn = nums[0]
    total_max = nums[0]
    for i in range(1, length):
        temp_maxx = maxx*nums[i]
        temp_minn = minn*nums[i]
        maxx = max(temp_maxx, temp_minn, nums[i])
        minn = min(temp_maxx, temp_minn, nums[i])
        total_max = max(maxx, total_max)
    return total_max

if __name__ == "__main__":
    nums = [-4, -3]
    print(max_pro(nums)) 

