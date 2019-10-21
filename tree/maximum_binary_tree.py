"""654. Make a maximum binary tree. T - O(n2), S - O(n2)"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def max_tree(arr):
    if not arr:
        return None
    length = len(arr)  
    # get the index of the max element in the array (pythonic)   
    max_index = arr.index(max(arr))
    maxx = max(arr)
    # make a node out of the max element
    root = TreeNode(maxx)
    # check whether the max element is the leftmost element of the curr array
    if max_index == 0:
        left_arr = []
    else:
        # select the left sub-array
        left_arr = arr[0:max_index]
    # check whether the max element is the right most element of the curr array 
    if max_index == length - 1:
        right_arr = []
    else:
        # select the right sub-array
        right_arr = arr[max_index+1:length]
    # make the left and right recursive calls on respective sub-arrays
    root.left = max_tree(left_arr)
    root.right = max_tree(right_arr)
    return root

if __name__ == "__main__":
    arr = [3, 2, 1, 6, 0, 5]
    root = max_tree(arr)
    print(root.val, root.left.val, root.right.val, root.right.left.val, root.left.right.val, root.left.right.right.val)