# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head 
        listLen  = 0 

        # calculate the length of the list 
        while cur: 
            listLen += 1 
            cur  = cur.next 

        step = listLen//k 
        mod = listLen % k 
        ans = []

        while len(ans) < k: 
            d = ListNode()
            d.next = head 
            if mod > 0: 
                for i in range(step):
                    if head:  
                        head = head.next
                    else: 
                        break  
            else: 
                for i in range(step-1):
                    if head:  
                        head = head.next
                    else: 
                        break

            next = head.next if head else None
            if head: 
                head.next = None
            head = next 

            ans.append(d.next)
            mod -= 1 
        return ans






        