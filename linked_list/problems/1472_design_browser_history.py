# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

# Implement the BrowserHistory class:

# BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
# void visit(string url) Visits url from the current page. It clears up all the forward history.
# string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

class ListNode:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.list = ListNode(homepage)
    
    def visit(self, url: str) -> None:
        self.list.next = ListNode(url, self.list)
        self.list = self.list.next
        
    def back(self, steps: int) -> str:
        while self.list.prev and steps > 0:
            self.list = self.list.prev
            steps -= 1
        return self.list.val

    def forward(self, steps: int) -> str:
        while self.list.next and steps > 0:
            self.list = self.list.next
            steps -= 1
        return self.list.val

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head, self.tail = ListNode(), ListNode()
        self.curr = ListNode(homepage,self.tail,self.head)
        self.head.next = self.tail.prev = self.curr
        
    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url,self.tail,self.curr)
        self.tail.prev = self.curr.next
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        i = 0
        while self.curr.prev != self.head and i < steps:
            self.curr = self.curr.prev
            i += 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        i = 0
        while self.curr.next != self.tail and i < steps:
            self.curr = self.curr.next
            i += 1
        return self.curr.val