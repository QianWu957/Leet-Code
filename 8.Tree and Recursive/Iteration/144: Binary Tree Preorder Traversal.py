# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root: return []

        queue = deque([root])
        while queue:
            node = queue.popleft()
            self.res.append(node.val)
            if node.right:
                queue.insert(0, node.right)
                

            if node.left:
                queue.insert(0, node.left)
        return self.res

        # self.res.append(root.val)
        # self.preorderTraversal(root.left)
        # self.preorderTraversal(root.right)

        # return self.res

