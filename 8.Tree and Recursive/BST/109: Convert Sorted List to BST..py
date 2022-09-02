# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        def conv_array_bst(nums):
            if len(nums) < 1: return None
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = conv_array_bst(nums[:mid])
            root.right = conv_array_bst(nums[mid+1:])
            return root
        return conv_array_bst(nums)

        
