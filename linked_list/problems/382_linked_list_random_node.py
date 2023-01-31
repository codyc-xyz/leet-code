# Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

# Implement the Solution class:

# Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
# int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.list = count = head
        self.size = 1
        while count:
            count = count.next
            self.size += 1


    def getRandom(self) -> int:
        curr = self.list
        if self.size > 1:
            steps = random.randrange(1, self.size) - 1
            while curr and steps > 0:
                curr = curr.next
                steps -= 1
        return curr.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()