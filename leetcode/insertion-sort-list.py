# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            j = head
            while j != cur:
                if j.val > cur.val: 
                    j.val, cur.val = cur.val, j.val
                j = j.next
            cur = cur.next
        return head
        