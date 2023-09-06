# Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

# The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

# Return an array of the k parts.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        arr = []
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        
        carry = length - k * (length // k) 
        res = length // k
        curr = head
        R = res
        while curr:
            if curr and R > 0:
                arr.append(curr)
                while curr and R > 1:
                    curr = curr.next
                    R -= 1
                if curr and carry:
                    curr = curr.next
                    carry -= 1
            elif curr and carry:
                arr.append(curr)
                carry -= 1
            if curr:
                nxt = curr.next
                curr.next = None
                curr = nxt
                R = res
        
        n = len(arr)
        while n < k:
            arr.append(curr)
            n += 1
        return arr
    

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1

        lenModK = length % k
        lenDivK = int(length / k)
        ans = []
        curr = head
        while curr:
            ans.append(curr)
            K = lenDivK
            while K > 0 and curr:
                prev = curr
                curr = curr.next
                K -= 1
            if lenModK > 0 and curr:
                lenModK -= 1
                prev = curr
                curr = curr.next
            if prev:
                prev.next = None

        while len(ans) < k:
            ans.append(None)
        return ans
