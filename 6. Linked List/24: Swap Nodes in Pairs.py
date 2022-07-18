class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        dummy = ListNode()
        dummy.next = head
        p = dummy
        

        while head and head.next:
            first = head
            second = head.next

            p.next = second

            first.next = second.next
            second.next = first
            p = first

            head = first.next

        return dummy. next


