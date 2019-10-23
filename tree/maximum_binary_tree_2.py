"""Maximum Binary Tree - Time Complexity - O(n2) or (nlogn), Space Complexity - O(n) or O(logn)"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# linear search to get the index of the array    
def get_max_index(arr, l, r):
    max_index = l
    for i in range(l, r):
        if arr[max_index] < arr[i]:
            max_index = i
    return max_index

# util function to apppy rexursion on array. Passing indices (left and right) to direct the recursion. 
def max_tree_util(arr, l, r):
    # base case: when max index and left index are same or right index and max_index+1 are same
    if l == r:
        return None
    # get the index of the max element in the array
    max_index = get_max_index(arr, l, r)
    # make the node with the corresponding max value of array
    root = TreeNode(arr[max_index])
    # make a recursive call to the left par the max index
    root.left = max_tree_util(arr, l, max_index)
    # make arecursive call to the right part of the max index
    root.right = max_tree_util(arr, max_index+1, r)
    return root

# main function to call the uti function with suitable indices (0 and length)
def max_tree(arr):
    return max_tree_util(arr, 0, len(arr))

if __name__  == "__main__":
    arr = [3, 2, 1, 6, 0, 5]
    root = max_tree(arr)
    print(root.val, root.left.val, root.right.val, root.right.left.val, root.left.right.val, root.left.right.right.val)