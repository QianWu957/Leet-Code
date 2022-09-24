# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if(n==0):
            return []
        # res = []
        def build_Trees(left,right):
            all_tree = []
            if left > right:
                return [None]

            for i in range(left, right+1):
                left_tree = build_Trees(left, i-1)
                right_tree = build_Trees(i+1, right)

                for l in left_tree:
                    for r in right_tree:
                        cur_tree = TreeNode(i)
                        cur_tree.left = l
                        cur_tree.right = r
                        all_tree.append(cur_tree)

            return all_tree
        
        # res = build_Trees(1,n)
        return build_Trees(1,n)
            
         