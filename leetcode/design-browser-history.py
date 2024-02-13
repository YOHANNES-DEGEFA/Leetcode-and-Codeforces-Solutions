class ListNode: 
    def __init__(self,val, next=None, prev=None): 
        self.val = val 
        self.next = next     
        self.prev = prev 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = ListNode(homepage)

    def visit(self, url: str) -> None:

        prev = self.homepage
        newNode = ListNode(url)
        newNode.prev = prev

        self.homepage.next = newNode
        self.homepage = self.homepage.next 
        

    def back(self, steps: int) -> str:

        while self.homepage.prev and steps > 0: 
            steps -= 1
            self.homepage = self.homepage.prev

        return self.homepage.val 
        

    def forward(self, steps: int) -> str:

        while self.homepage.next and steps > 0: 
            steps -= 1 
            self.homepage = self.homepage.next

        return self.homepage.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)