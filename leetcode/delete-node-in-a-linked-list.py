# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node and node.next: 
         
            node.val = node.next.val
            if not node.next.next: 
                node.next = None  
                break
            node = node.next
           
                
            
        
        
        