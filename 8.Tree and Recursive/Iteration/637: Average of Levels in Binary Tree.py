# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import deque
        
        if not root: return []
        queue = deque([root])
        level = 0
        while queue:
            self.res.append([])
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                self.res[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            level +=1

        return [mean(a) for a in self.res]




            

            


