# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return []
    
        def rootSum(root, path):
            if not root: return []
            if not root.left and not root.right:
                self.res.append(path+[str(root.val)])
            rootSum(root.left, path+[str(root.val)])
            rootSum(root.right, path+[str(root.val)])

        rootSum(root, [])
        return sum(int(''.join(path)) for path in self.res)


