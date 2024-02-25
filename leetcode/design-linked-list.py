
class Node: 
    def __init__(self,val=0):
        self.val = val 
        self.next = None

class MyLinkedList:

    def __init__(self,val=0, next=None):

        self.head = Node()
        self.length = 0 
        

    def get(self, index: int) -> int:

        if index >= self.length: 
            return -1

        # n v 
        if not self.head.next: 
            return -1 

        cur_node = self.head.next   # added .next  
        for _ in range(index):
            cur_node = cur_node.next 

        return cur_node.val  # removed if cur_node else -1

    def addAtHead(self, val: int) -> None:
        dummy = Node(val)
        dummy.next = self.head.next
        self.head.next = dummy 
        self.length += 1 
  
    def addAtTail(self, val: int) -> None:
        if not self.head.next:    # added .next 
            self.head.next = Node(val)
        else: 
            cur = self.head   # might have bug 
            while cur.next: 
                cur = cur.next 

            cur.next  = Node(val)
        self.length +=  1
            
                
        

    def addAtIndex(self, index: int, val: int) -> None:
        if self.length < index:   # index < 0 not included why 
            return 
        
        
        if index == 0:   
            self.addAtHead(val)
          

        elif index == self.length:     # different one 
            self.addAtTail(val)
         
        else: 
            cur_node = self.head.next   # added .next 
            for _ in range(index-1): 
                cur_node  = cur_node.next 
            tmp = cur_node.next        # hold the reference to the next node 
            cur_node.next = Node(val)   # inserte the new node 
            cur_node.next.next = tmp        
        
            self.length += 1  # for some reason this thing is under the else condition  my first code was buggy because I was incrementing self.legnth out side of the else condition this was not correct coz self.length is being increment 2 in the case the conditions before the else True
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:   # if this thing is 1-indexed this might cause a problem 
            return 
        if index == 0: 
            self.head.next = self.head.next.next  # added .next  .next 
        else: 
            prev = None
            curr = self.head.next
            for _ in range(index):
                prev = curr
                curr = curr.next
            prev.next = curr.next
        self.length -= 1

        # Bravo Jo!
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)