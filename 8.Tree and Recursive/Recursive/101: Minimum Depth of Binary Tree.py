# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        # if not root.left and not root.right: return 1

        # left_depth = self.minDepth(root.left)
        # right_depth = self.minDepth(root.right)

        # if not root.left or not root.right:
        #     return max(left_depth, right_depth)+1
        # return min(left_depth,right_depth)+1

        que = collections.deque([(root,1)])
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left,depth+1))
            if node.right:
                que.append((node.right, depth +1))
        

        

