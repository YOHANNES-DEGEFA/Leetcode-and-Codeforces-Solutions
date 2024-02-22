class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
       
        self.head = Node(0)
        self.rear = self.head
        self.k = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
       
        if self.size == self.k:
            return False
        else:
            node = Node(value)
            
            self.rear.next = node
            self.rear = node
            self.size += 1
            return True
        

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        else: 
            if self.head.next.next is None:
                self.rear = self.head

            self.head.next = self.head.next.next
            self.size -= 1
            return True
        

    def Front(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.head.next.val
        

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.rear.val


    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


