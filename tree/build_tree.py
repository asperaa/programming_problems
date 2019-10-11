"""Build Tree using inorder and pre order"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BuildTree:
    def __init__(self):
        self.idx = 0
    
    def build_tree_util(self, in_order, pre_order, in_dict, in_left, in_right):
        if in_left == in_right:
            return None
        root = TreeNode(pre_order[self.idx])
        partition_index = in_dict[root.val]
        self.idx += 1
        root.left = self.build_tree_util(in_order, pre_order, in_dict, in_left, partition_index)
        root.right = self.build_tree_util(in_order, pre_order, in_dict, partition_index+1, in_right)
        return root
    
    def build_tree(self, in_order, pre_order):
        in_dict = {val: idx for idx, val in enumerate(in_order)}
        return self.build_tree_util(in_order, pre_order, in_dict, 0, len(in_order))

if __name__ == "__main__":
    pre_order = [3, 9, 20, 15, 7]
    in_order = [9, 3, 15, 20, 7]
    BT = BuildTree() 
    print(BT.build_tree(in_order, pre_order).val)