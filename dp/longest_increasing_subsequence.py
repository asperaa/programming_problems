"""Longest increasing subsequqnce. Brute Force. Time - O(pow(2, n)). Exponential"""
def lis_util(arr, previous, curr_pos):
    if curr_pos == len(arr):
        return 0
    include_curr = 0
    if arr[curr_pos] > previous:
        include_curr = 1 + lis_util(arr, arr[curr_pos], curr_pos+1)
    not_include_curr = lis_util(arr, previous, curr_pos+1)
    return max(include_curr, not_include_curr)

    
    
    
    

def lis(arr):
    return lis_util(arr, float('-inf'), 0) 
    
if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    arr2 = [1,3,6,7,9,4,10,5,6]

    print(lis(arr2))
