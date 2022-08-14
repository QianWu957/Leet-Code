# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        def helper(root):
            if not root: return 0
            left_length = helper(root.left)
            right_length = helper(root.right)
            if root.left:
                if root.val == root.left.val:
                    left_length +=1
                else:
                    left_length = 0

            if root.right:
                if root.val == root.right.val:
                    right_length +=1
                else:
                    right_length = 0

            self.res = max(self.res, left_length + right_length)
            return max(left_length,right_length)

        helper(root)
        return self.res

      