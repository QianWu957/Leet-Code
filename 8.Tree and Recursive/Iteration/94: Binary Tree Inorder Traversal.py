# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            self.res.append(cur.val)
            cur = cur.right
        return self.res


        # from collections import deque
        # if not root: return []
        # queue = deque([root])

        # while queue:
        #     node = queue.popleft()
            
        #     if node.right:
        #         queue.insert(0, node.right)
            
        #     self.res.append(node.val)

        #     if node.left:
        #         queue.insert(0,node.left)
            

        # return self.res

            


        # self.inorderTraversal(root.left)
        # self.res.append(root.val)
        # self.inorderTraversal(root.right)

        # return self.res