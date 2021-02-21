class Solution(object):
    def __init__(self):
        self.curr  = None
        self.v = True
    def isValidBST(self, root: TreeNode) -> bool:
    
        if root == None:
            return 
        self.isValidBST(root.left)
        if self.v == None:
            self.curr = root.val
        elif self.curr >= root. val:
            self.v = False
        else:
           self.curr = root.val
        self.isValidBST(root.right)
        
        return self.v
