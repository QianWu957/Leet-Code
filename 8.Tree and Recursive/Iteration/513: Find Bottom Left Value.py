class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        if not root: return
        queue = deque([root])
        while queue:
            res = []
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                if len(res) == 0:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res[0]
        