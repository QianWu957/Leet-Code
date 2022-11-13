# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        left_root = root
        right_root = root
        left_depth = 0
        right_depth = 0

        while left_root:
            left_root = left_root.left
            left_depth +=1
        while right_root:
            right_root = right_root.right
            right_depth +=1
        if left_depth ==  right_depth:
            return 2**left_depth-1

        else:
            return self.countNodes(root.left)+self.countNodes(root.right) +1 



    # def __init__(self):
    #     self.res = 0
    # def countNodes(self, root: Optional[TreeNode]) -> int:
    #     if not root: return 0
    #     self.res +=1
    #     self.countNodes(root.left)
    #     self.countNodes(root.right)
    #     return self.res

    

