# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def dfs(root1, root2, is_odd_level):
            if not root1:
                return
            
            if is_odd_level:
                root1.val, root2.val = root2.val, root1.val
            
            dfs(root1.left, root2.right, not is_odd_level)
            dfs(root1.right, root2.left, not is_odd_level)

        dfs(root.left, root.right, True)

        return root