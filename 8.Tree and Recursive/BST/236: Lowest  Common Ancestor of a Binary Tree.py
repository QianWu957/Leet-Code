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

        def findAncestor(root):
            if not root: return
            if p == root or q == root:
                return root

            left = findAncestor(root.left)
            right = findAncestor(root.right)

            if left and right:
                return root
            
            return left if left else right

        return findAncestor(root)


