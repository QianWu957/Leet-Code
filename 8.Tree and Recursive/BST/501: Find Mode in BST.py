# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inordertrav(root):
            if not root: return

            inordertrav(root.left)
            self.res.append(root.val)
            inordertrav(root.right)

        inordertrav(root)
        # print(self.res)

        hashmap = {}
        ans = []

        for i in range(len(self.res)):
            if self.res[i] not in hashmap:
                hashmap[self.res[i]] = 1
            else:  
                hashmap[self.res[i]]+=1
        # print(hashmap)
        max_ = max(hashmap.values())
        # print(max_)
        for k,v in hashmap.items():
            if v == max_:
                ans.append(k)
        return ans

        

