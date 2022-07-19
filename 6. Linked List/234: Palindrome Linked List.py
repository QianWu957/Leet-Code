# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #by using array
        if not head: return True
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        front, back = 0, len(nums)-1
        while front <= back:
            if nums[front] != nums[back]:
                return False
            else:
                front+=1
                back-=1
        return True

        #by using stack
        if not head: return True
        s = []
        p = head
        while p:
            s.append(p.val)
            p = p.next
        # print(s)

        while head:
            if head.val != s.pop():
                return False
            head = head.next
        return True