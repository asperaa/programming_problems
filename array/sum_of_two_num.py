def twoSum(nums, target):
    hash_dict = dict()
    for i, num in enumerate(nums):
        hash_dict[target-num] = i
    
    for i in range(len(nums)):
        if nums[i] in hash_dict:
            if i != hash_dict[nums[i]]:
                return [i, hash_dict[nums[i]]]