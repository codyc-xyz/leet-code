# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.

# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.

# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:

# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. 
# If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        i = 0
        curr = self.head.next
        while i < index:
            curr = curr.next
            i += 1
        return curr.val

    def addAtHead(self, val: int) -> None:
        prevHead = self.head.next
        self.head.next = ListNode(val, prevHead, self.head)
        prevHead.prev = self.head.next
        self.size += 1

    def addAtTail(self, val: int) -> None:
        prevTail = self.tail.prev
        self.tail.prev = ListNode(val, self.tail, prevTail)
        prevTail.next = self.tail.prev
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        i = 0
        curr = self.head
        while curr and i < index:
            curr = curr.next
            i += 1
        prev, nxt = curr, curr.next
        prev.next = ListNode(val, nxt, prev)
        if nxt:
            nxt.prev = prev.next
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        i = 0
        curr = self.head
        while curr and i < index:
            curr = curr.next
            i += 1
        if curr and curr.next:
            prev, nxt = curr, curr.next.next
            if nxt:
                prev.next = nxt
                nxt.prev = prev
            else:
                prev.next = None
            self.size -= 1

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, next=self.head)
        if self.tail is None:
            self.tail = new_node
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        if index == 0:
            self.addAtHead(val)
            return
        curr = self.head
        i = 0
        while curr:
            if i == index-1:
                new_node = ListNode(val, next=curr.next)
                curr.next = new_node
                if new_node.next is None:
                    self.tail = new_node
                break
            curr = curr.next
            i += 1
        if i < index-1:
            return -1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        curr = self.head
        i = 0
        while curr:
            if i == index-1:
                if curr.next is None:
                    return
                curr.next = curr.next.next
                if curr.next is None:
                    self.tail = curr
                break
            curr = curr.next
            i += 1
        if i < index-1:
            return -1