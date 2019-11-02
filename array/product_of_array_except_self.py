"""Product of array except self. Time - O(n). Space - O(n)"""
class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        p = 1
        length = len(nums)
        for i in range(length):
            result.append(p)
            p = p*nums[i]
        p = 1
        for i in range(length-1, -1, -1):
            result[i] = result[i]*p
            p = p*nums[i]
        
        return result
        