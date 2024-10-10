# Node Class:
class TreeNode:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


maxx = 0
minn = 0
node_hd = {}
hd_dict = {}

def bottom_view_util(root, hd):
    
    # declare the global constants
    global maxx
    global minn
    global node_hd
    global hd_dict
    
    node_hd[root] = hd # data keeping for the root
    
    minn = min(minn, hd) # maintain the min and max values for the BT
    maxx = max(maxx, hd) 
    
    if hd not in hd_dict:
        hd_dict[hd] = [root.val]
    else:
        hd_dict[hd].append(root.val)
    
    bottom_view_util(root.left, hd-1)
    bottom_view_util(root.right, hd+1)
    
    
def bottomView(root):
    '''
    :param root: root of the binary tree
    :return: None, newline is provided by driver code
    '''
    bottom_view_util(root, 0)

    for i in range(minn, maxx+ 1):
        print(hd_dict[i][-1], end=" ")
    return None

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(bottomView(root))