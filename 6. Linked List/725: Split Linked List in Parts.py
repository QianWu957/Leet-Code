# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        dummy = ListNode()
        dummy.next = head
        p , p1 = head, head
        res = []
        length = 0
        while p:
            length+=1
            p = p.next
        
        quotient = length // k
        remainder = length % k

        print(length, quotient, remainder)
        i = 0
        while k:
            if i < remainder:
                sub_length = quotient+1
            else:
                sub_length = quotient
            if sub_length:
                p2 = p1
                while sub_length-1 != 0:
                    p1 = p1.next
                    sub_length-=1
                temp = p1.next
                p1.next = None
                res.append(p2)
                p1 = temp
            else:
                res.append(None)
            k -= 1
            i += 1
        return res

