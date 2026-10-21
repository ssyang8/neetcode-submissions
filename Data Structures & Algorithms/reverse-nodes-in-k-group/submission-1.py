# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        def reverse(start, end):
            prev = ListNode()
            while start != end:
                startNext = start.next
                start.next = prev
                prev = start
                start = startNext
            
            return prev

        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while True:
            curHead = cur.next
            node = cur
            for i in range(k):
                if node:
                    node = node.next
                else:
                    return dummy.next
            
            nextHead = node.next

            newHead = reverse(curHead, nextHead)
            cur.next = newHead
            curHead.next = nextHead
        

        