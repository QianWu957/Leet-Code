# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        cur = head
        # print(cur)
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head

        # if not head: return head

        # slower, faster = head, head.next

        # # while faster:

        # while faster and slower.val == faster.val:

        #     ## 如果faster对应的元素与slower对应的元素相同
        #     # faster后移直到指向不同的元素或者遍历完链表
        #     # if slower.val == faster.val:
        #     faster = faster.next

        #     ## 去除中间重复的元素
        #     slower.next = faster
        #     # 如果faster遍历结束链表，结束
        #     if not faster: break
        #     # 将快慢指针同步后移
        #     faster = faster.next
        #     slower = slower.next
        #     # print(slower)
        # return head

        
        
        
