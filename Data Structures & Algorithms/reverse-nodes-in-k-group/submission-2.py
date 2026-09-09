# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node, end):
            prev = None
            cur = node
            while cur != end:
                curNext = cur.next
                cur.next = prev
                prev = cur
                cur = curNext
            return prev
        dummy = ListNode()
        dummy.next = head
        fast = dummy
        while True:
            slow = fast
            for _ in range(k):
                fast = fast.next
                if fast is None:
                    return dummy.next
            nextGroupHead = fast.next
            curGroupEnd = slow.next
            curGroupHead = reverse(curGroupEnd, nextGroupHead)
            slow.next = curGroupHead
            curGroupEnd.next = nextGroupHead
            fast = curGroupEnd
        

