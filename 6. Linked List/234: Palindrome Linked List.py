# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # dummy = ListNode()
        # dummy.next = head
        # p = head

        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        # print(nums)
        # if len(nums) == 1:
        #     return True

        front, back = 0, len(nums)-1
        
        while front <= back:
            if nums[front] != nums[back]:
                return False
            else:
                front+=1
                back-=1
        return True