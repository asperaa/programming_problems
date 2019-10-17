"""Build a tree from post_order and in_order traversal"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class BuildTree:
    def __init__(self):
        self.in_order_index = dict()
        self.length = 0
        self.idx = self.length - 1
        
    
    def build_tree_helper(self, post_order, lower, upper, counter):
        if lower == upper:
            return None
        value = post_order[self.idx]
        self.idx -= 1
        middle_index = self.in_order_index[value]
        root = TreeNode(value)
        
        root.right = self.build_tree_helper(post_order, middle_index+1, upper, counter + 1)
        root.left = self.build_tree_helper(post_order, lower, middle_index, counter + 1)
        
        return root
    
    def build_tree(self, in_order, post_order):
        self.in_order_index = {value: index for index, value in enumerate(in_order)}
        self.length = len(in_order)
        return self.build_tree_helper(post_order, 0, self.length, 0)

if __name__ == "__main__":
    in_order = [9, 3, 15, 20, 7]
    post_order = [9, 15, 7, 20, 3]

    BT = BuildTree()
    print(BT.build_tree(in_order, post_order).val)