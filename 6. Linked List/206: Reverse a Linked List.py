class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        # if not head: return None 
        
        # prev, curr = None, head

        # while curr != None:
        #     nex = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nex
        # return prev

        if not head or not head.next:
            return head
        nextNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        # print(nextNode)
        return nextNode    
      

if __name__ == '__main__':
    a = Solution()
    n = [1,2,3,4,5]
    print(a.reverseList(n))


