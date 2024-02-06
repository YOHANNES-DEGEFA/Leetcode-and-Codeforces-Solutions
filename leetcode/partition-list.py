# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        answer = less = ListNode()
        greaterEqualHead = greaterEqual = ListNode()

        while head: 
            if head.val < x: 
                less.next = head
                less = less.next 
            else: 
                greaterEqual.next = head 
                greaterEqual = greaterEqual.next
            head = head.next
        greaterEqual.next = None 
        less.next = greaterEqualHead.next
        return answer.next 
        