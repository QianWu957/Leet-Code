# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        head = dummy
        if not l1: return l2
        if not l2: return l1

        s1, s2, res = [],[],[]
        while l1:
            s1.append(l1.val)
            l1 = l1.next
            # print(s1)
        
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        # print(s1)
        # print(s2)
        carryout = 0
        while s1 or s2:
            if s1:
                num1 = s1.pop()
                # print(s1)
            else:
                num1 = 0
            if s2:
                num2 = s2.pop()
                # print(s2)
            else:
                num2 = 0
            num = (num1+num2+carryout)%10
            carryout = (num1+num2+carryout)//10
            res.append(num)
        if carryout !=0:
            res.append(carryout)
        print(res)
        while res:
            head.next = ListNode(res.pop())
            head = head.next
        return dummy.next
