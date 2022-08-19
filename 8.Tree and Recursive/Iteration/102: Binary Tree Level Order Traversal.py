# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root: return []
        queue = deque([root])
        # level_length = len(queue)
        level = 0
        while queue:
            self.res.append([]) #1
            level_length = len(queue)
            # node = queue.popleft()
            for i in range(level_length):
                node = queue.popleft() #2
                self.res[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return self.res

            

        # if not root: return self.res

        # def levelCounter(root,level):
        #     if not root: return 
        #     if len(self.res) == level:
        #         self.res.append([]) 
        #     self.res[level].append(root.val) 

        #     levelCounter(root.left, level+1)
        #     levelCounter(root.right, level+1)

        # levelCounter(root, 0)
        # return self.res
