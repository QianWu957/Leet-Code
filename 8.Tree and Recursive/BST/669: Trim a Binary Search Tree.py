# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root: return

        def trim(root):
            if not root: return
            if root.val > high:
                root = trim(root.left)
            elif root.val < low:
                root = trim(root.right)
            else:
                root.left = trim(root.left)
                root.right = trim(root.right)
            return root
        
        return trim(root)
