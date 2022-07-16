class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or headB: return None

        hashmap = set()

        while headA:
            hashmap.add(headA)
            headA  = headA.next

        while headB:
            if headB in hashmap:
                return headB
            headB = headB.next

if __name__ == '__main__':
    a = Solution()
    8
    [4,1,8,4,5]
    [5,6,1,8,4,5]
    2
    3
