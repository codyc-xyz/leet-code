# You are given the head of a linked list.

# The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). The length of a group is the number of nodes assigned to it. In other words,

# The 1st node is assigned to the first group.
# The 2nd and the 3rd nodes are assigned to the second group.
# The 4th, 5th, and 6th nodes are assigned to the third group, and so on.

# Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.

# Reverse the nodes in each group with an even length, and return the head of the modified linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        arr = [[]]
        i = 0
        while curr:
            if len(arr[i]) > i:
                arr.append([])
                i += 1
            arr[i].append(curr.val)
            curr = curr.next
         
        ans = dummy = ListNode()
        for i in range(len(arr)):
            if not len(arr[i]) % 2:
                for n in arr[i][::-1]:
                    dummy.next = ListNode(n)
                    dummy = dummy.next
            else:
                for n in arr[i]:
                    dummy.next = ListNode(n)
                    dummy = dummy.next
                
        return ans.next