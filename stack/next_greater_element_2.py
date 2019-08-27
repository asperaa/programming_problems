"""Slight modification of next_greater_1"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        length = len(nums2)
        stack = []
        stack.append(nums2[-1])
        result = [None]*len(nums1)
        cache = dict()
        cache[nums2[-1]] = -1
        
        for i in range(length - 2, -1, -1):
            if len(stack) == 0:
                stack.append(nums2[i])
                cache[nums2[i]] = -1
                continue
            if nums2[i] < stack[-1]:
                cache[nums2[i]] = stack[-1]
                stack.append(nums2[i])
                continue
            while len(stack)!= 0 and nums2[i] > stack[-1]:
                stack.pop()
            if len(stack) == 0:
                cache[nums2[i]] = -1
                stack.append(nums2[i])
            else:
                cache[nums2[i]] = stack[-1]
                stack.append(nums2[i])
        
        for i in range(len(nums1)):
            result[i] = cache[nums1[i]]
        return result
            
                
                
                
                