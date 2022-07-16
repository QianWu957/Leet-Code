# Definition for singly-linked list.
from regex import P


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1:[ListNode], list2:[ListNode]) -> [ListNode]:

        dummyNode = ListNode()
        pre_head = dummyNode

        while list1 and list2:

            if list1.val < list2.val:
                dummyNode.next = list1
                list1 = list1.next
                dummyNode = dummyNode.next

            else:
                dummyNode.next = list2
                list2 = list2.next
                dummyNode = dummyNode.next

        if list1:
            dummyNode.next = list1

        elif list2:
            dummyNode.next = list2
        return pre_head.next
        
def list_to_node(nums):
    if not nums:
        return None
    p = ListNode(nums[0])
    head = p
    for i in range(1, len(nums)):
        p.next = ListNode(nums[i])
        p = p.next
    return head

def linklist_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res
        
if __name__ == '__main__':
    a = Solution()
    l1 = [1,2,4]
    l2 = [1,3,4]
    l1 = list_to_node(l1)
    l2 = list_to_node(l2)
    # print(l1.next.val)
    print(linklist_to_list(a.mergeTwoLists(l1, l2)))
