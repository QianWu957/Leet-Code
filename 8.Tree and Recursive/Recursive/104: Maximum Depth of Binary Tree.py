# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        left_length = self.maxDepth(root.left)
        right_length = self.maxDepth(root.right)

        return max(left_length, right_length)+1

if __name__ == '__main__':
    a = Solution()
    n = [3,9,20,null,null,15,7]
    print(a.maxDepth(n))

