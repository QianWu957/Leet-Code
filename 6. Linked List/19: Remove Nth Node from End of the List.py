# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return head
        
        dummy = ListNode()
        dummy.next = head

        p1 = dummy
        p2 = dummy

        for i in range(n):
            p2 = p2.next
        
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        
        p1.next = p1.next.next
        #test
        return dummy.next



        
        
            
        
        
        