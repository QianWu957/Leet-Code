# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def indordertrav(root):
            if not root: return 

            indordertrav(root.left)
            self.res.append(root.val)
            indordertrav(root.right)
            # print(self.res)

        indordertrav(root)

        head, tail = 0, len(self.res)-1

        while head<tail:
            if self.res[head] + self.res[tail] == k: return True

            elif self.res[head] + self.res[tail] > k:
                tail-=1
            elif self.res[head] + self.res[tail] < k:
                head+=1

        return False