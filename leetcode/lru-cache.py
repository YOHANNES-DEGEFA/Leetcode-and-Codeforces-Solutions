class Node: 
    def __init__(self,key=-1,val=-1): 
        self.key = key
        self.val = val 
        self.next = None 
        self.prev = None 


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.map = {}
        self.head = Node()
        self.tail = Node()

        self.tail.prev = self.head 
        self.head.next = self.tail 
        

    def get(self, key: int) -> int:
        if key not in self.map: 
            return -1 

        node = self.map[key]

        self.take_from_middle(key)
        self.add_to_end(node.key,node.val)

        return node.val


        

    def put(self, key: int, value: int) -> None:

        if key in self.map: 
            self.take_from_middle(key)
            self.add_to_end(key,value)
        else:

            if len(self.map) == self.capacity: 
                del self.map[self.head.next.key]
                self.head.next = self.head.next.next 
                self.head.next.prev = self.head 

            self.add_to_end(key,value)

    def add_to_end(self,key,val): 
        newNode = Node(key,val)

        newNode.prev = self.tail.prev 
        self.tail.prev = newNode 
        newNode.prev.next = newNode 
        newNode.next = self.tail

        self.map[key] = newNode

    def take_from_middle(self,key):
        node = self.map[key]

        #put the node out from the middle and distribute its pointers accordingly 
        node.prev.next = node.next
        node.next.prev = node.prev



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)