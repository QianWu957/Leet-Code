# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def bfsInorder(root):
            stack = []
            cur = root
            while stack or cur:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop()
                self.res.append(cur.val)
                cur = cur.right
        bfsInorder(root)
        print(self.res)

        dif_col = []
        for i in range(len(self.res)-1):
            dif_col.append(self.res[i+1] - self.res[i])
        return min(dif_col)

