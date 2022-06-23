# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        if not head or not head.next: return False
        
        slow, fast = head, head.next
        
        while slow and fast:
            if slow == fast:
                return True
            
            if fast.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return False 
        return False 

if __name__ == "__main__":
    a = Solution()
    h = [3,2,0,-4]
    # head_prev = ListNode(-1)
    
    head = ListNode(h[0])
    
    i = 1
    cur = head
    while i < len(h):
        cur.next = ListNode(h[i])
        cur = cur.next
        i += 1
    cur.next = head.next
    print (a.hasCycle(head))
