# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum_ = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        if not root: return
        def inordertrav(root):
            if not root: return
            inordertrav(root.right)
            self.sum_ += root.val
            root.val = self.sum_
            inordertrav(root.left)
            return root
            
        res = inordertrav(root)
        return res

        # stack = []
        # cur = root
        # while stack or cur:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left

        #     cur = stack.pop()
        #     self.res.append(cur.val)
        #     cur = cur.right
        
        # print(self.res)