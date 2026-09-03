# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        left = head
        right = head
        cnt = 0
        while cnt<n:
            right = right.next
            cnt += 1

        while right and right.next:
            left = left.next
            right = right.next

        if right is None:
            return head.next
            
        nex = left.next

        left.next = nex.next
        nex.next = None

        return head