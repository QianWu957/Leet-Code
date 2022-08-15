class Solution:
    def __init__(self):
        self.res = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        def rootSum(root, path, targetSum):
            if not root: return []
            targetSum -= root.val
            if not root.left and not root.right and targetSum == 0:
                return self.res.append(path + [root.val])
            rootSum(root.left, path+[root.val], targetSum)
            rootSum(root.right, path+[root.val], targetSum)

        rootSum(root, [], targetSum)

        return self.res

