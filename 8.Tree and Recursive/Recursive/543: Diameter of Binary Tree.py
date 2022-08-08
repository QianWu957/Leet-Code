class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def helper(root):
            if not root: return 0

            left_length = helper(root.left)
            right_length = helper(root.right)

            self.res = max(self.res, left_length + right_length)

            return max(left_length,right_length)+1

        self.res = 0
        helper(root)

        return self.res
    

