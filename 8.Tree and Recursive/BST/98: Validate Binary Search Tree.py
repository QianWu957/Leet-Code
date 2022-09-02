# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root: return

        def inordertrav(root):
            if not root: return 
            inordertrav(root.left)
            self.res.append(root.val)
            inordertrav(root.right)

        inordertrav(root)
        print(self.res)
        for i in range(len(self.res)-1):
            if self.res[i+1] <= self.res[i]:
                return False
        return True



