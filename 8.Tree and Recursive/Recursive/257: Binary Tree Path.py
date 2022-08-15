# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        self.res = []

        def helper(root, path):
            if not root: return
            if not root.left and not root.right: 
                self.res.append(path + [str(root.val)])
            helper(root.left, path+[str(root.val)])
            helper(root.right,  path + [str(root.val)])
        
        helper(root, [])
        print(self.res)
        return ['->'.join(path) for path in self.res]

