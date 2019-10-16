"""kth smallest element in bst. Space and time - O(n) """
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class KSmall:
    def __init__(self):
        self.arr = []
    
    def in_order(self, root):
        if not root:
            return None
        self.in_order(root.left)
        self.arr.append(root.val)
        self.in_order(root.right)
        return None
        

    def k_small(self, root, k):
        self.in_order(root)
        return self.arr[k-1]
        

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(4)
    KSmall = KSmall()
    print(KSmall.k_small(root, 1))
        
        
