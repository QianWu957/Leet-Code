# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.recur(root) >= 0

    def recur(self, root):
        if not root: return 0
        left = self.recur(root.left)
        if left == -1: return -1
        right = self.recur(root.right)
        if right == -1: return -1
        if abs(left - right) < 2:
            return max(left, right)+1
        else:
            return -1

    # def isBalanced(self, root: TreeNode) -> bool:
    #     def height(root: TreeNode) -> int:
    #         if not root:return 0
    #         leftHeight = height(root.left)
    #         rightHeight = height(root.right)
    #         if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
    #             return -1
    #         else:
    #             return max(leftHeight, rightHeight) + 1

    #     return height(root) >= 0



    # def maxDepth(self,root):
    #         if not root:return 0 
    #         return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
    


    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True
    #     return abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1 \
    #     and self.isBalanced(root.left) and self.isBalanced(root.right)   

