# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return 

        def findAncester(root):

            if p.val < root.val and q.val < root.val:
                findAncester(root.left)
            
            elif p.val > root.val and q.val > root.val:
                findAncester(root.right)

            else:
                self.res = root

            return
        findAncester(root)

        return self.res
