"""Find the number of path sums in whole tree"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class PathSumNum:
    
    def path_sum_util(self, root, sum, curr_sum, cache):
        if not root:
            return None
        curr_sum += root.val
        old_sum = curr_sum - sum
        
        if old_sum in cache:
            self.result += cache[old_sum]
        cache[curr_sum] = cache.get(curr_sum, 0) + 1

        self.path_sum_util(root.left, sum, curr_sum, cache)
        self.path_sum_util(root.right, sum, curr_sum, cache)

        cache[curr_sum] -= 1
    
    def path_sum_num(self, root, sum):
        
        if not root:
            return 0
        self.result = 0
        cache = {0:1}
        self.path_sum_util(root, sum, 0, cache)
        return self.result

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    # root.left.left = TreeNode(11)
    # root.left.left.left = TreeNode(7)
    # root.left.left.right = TreeNode(2)

    # root.right.left = TreeNode(13)

    # root.right.right = TreeNode(4)
    # root.right.right.left = TreeNode(5)
    # root.right.right.right = TreeNode(1)

    NPS = PathSumNum()
    print(NPS.path_sum_num(root, -1))  
