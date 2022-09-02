# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: reuturn

        def inordertrav(root):
            if not root: return
            inordertrav(root.left)
            self.res.append(root.val)
            inordertrav(root.right)

        inordertrav(root)
        return self.res[k-1]
        # if not root: return
        # stack = []
        # cur = root
        # while stack or cur:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
            
        #     cur = stack.pop()
        #     self.res.append(cur.val)
        #     cur = cur.right
 
        # return self.res[k-1]

        