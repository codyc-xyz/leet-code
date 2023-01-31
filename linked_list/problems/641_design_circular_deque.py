# Design your implementation of the circular double-ended queue (deque).

# Implement the MyCircularDeque class:
# MyCircularDeque(int k) Initializes the deque with a maximum size of k.
# boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
# int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
# int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
# boolean isEmpty() Returns true if the deque is empty, or false otherwise.
# boolean isFull() Returns true if the deque is full, or false otherwise.

class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.maxSize = k
        self.size = 0
        self.head = None
        self.tail = None
    def insertFront(self, value: int) -> bool:
        if self.size >= self.maxSize:
            return False
        if not self.head:
            self.tail = self.head = ListNode(value)
        else:
            tmp = self.head
            self.head = ListNode(value, next=tmp)
            tmp.prev = self.head
        self.size += 1
        return True
    def insertLast(self, value: int) -> bool:
        if self.size >= self.maxSize:
            return False
        if not self.tail:
            self.tail = self.head = ListNode(value)
        else:
            tmp = self.tail
            self.tail.next = ListNode(value, prev=tmp, next=None)
            self.tail = self.tail.next
        self.size += 1
        return True
    def deleteFront(self) -> bool:
        if self.head:
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:
            return False
        self.size -= 1
        return True
    def deleteLast(self) -> bool:
        if self.tail:
            if self.head == self.tail:
                self.head = None
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.tail = None
        else:
            return False
        self.size -= 1
        return True
        
    def getFront(self) -> int:
        if self.head:
            return self.head.val
        return -1

    def getRear(self) -> int:
        if self.tail:
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        return not self.head and not self.tail

    def isFull(self) -> bool:
        return self.size >= self.maxSize
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()