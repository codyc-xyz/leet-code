# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. 
# Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. 
# None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

# Your code will only be given the head of the original linked list.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {None:None}
        
        curr = head
        while curr:
            hm[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = hm[curr]
            copy.next = hm[curr.next]
            copy.random = hm[curr.random]
            curr = curr.next
        return hm[head]

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
       
        curr = head
        hm = {}

        while curr:
            hm[curr] = Node(curr.val)
            curr = curr.next

        ans = copy = Node(0)
        
        while head:
            copy.next = hm[head]
            copy.next.next = hm[head.next] if head.next else None
            copy.next.random = hm[head.random] if head.random else None

            copy = copy.next
            head = head.next

        return ans.next
    

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        hm = {}
        curr = curr2 = head

        while curr:
            hm[curr] = Node(curr.val)
            curr = curr.next

        while curr2:
            if curr2.next:
                hm[curr2].next = hm[curr2.next]
            if curr2.random:
                hm[curr2].random = hm[curr2.random]
            curr2 = curr2.next

        return hm[head] if head else None
