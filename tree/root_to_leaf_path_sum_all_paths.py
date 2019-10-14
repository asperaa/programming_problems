"""Path sum routes equal to root to leaves"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class PathSumAll:
    def __init__(self):
        self.path_sum = []
    
    
    def path_sum_all_util(self, root, sum, r_sum, route):
        if not root:
            return None
        r_sum += root.val
        
        if not root.left and not root.right:
            if r_sum == sum:
                route.append(root.val)
                self.path_sum.append(route)
                return None
        self.path_sum_all_util(root.left, sum, r_sum, route + [root.val])
        self.path_sum_all_util(root.right, sum, r_sum, route + [root.val])
        return None
    
    def path_sum_driver(self, root, sum):
        if not root:
            return self.path_sum
        route = []
        self.path_sum_all_util(root, sum, 0, route)
        return self.path_sum

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right.left = TreeNode(13)

    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    PS = PathSumAll()
    print(PS.path_sum_driver(root, 22))