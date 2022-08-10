# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
            self.res = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        if not root: return 0

        def rootSum(root,targetSum):
            if not root: return 0

            targetSum -= root.val
            if targetSum == 0:
                self.res +=1
            rootSum(root.left, targetSum)
            rootSum(root.right, targetSum)

        rootSum(root,targetSum)
        self.pathSum(root.left,targetSum)
        self.pathSum(root.right,targetSum)

        return self.res
