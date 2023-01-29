# A critical point in a linked list is defined as either a local maxima or a local minima.

# A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

# A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

# Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

# Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] 
# where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. 
# If there are fewer than two critical points, return [-1, -1].

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        critPoints = []
        prev, curr = head, head.next
        i = 1
        while curr and curr.next:
            if curr.val > prev.val and curr.val > curr.next.val or curr.val < prev.val and curr.val < curr.next.val:
                critPoints.append(i)
            curr = curr.next
            prev = prev.next
            i += 1
            
        if len(critPoints) > 1:
            maxima = max(critPoints) - min(critPoints)
            minima = maxima
            critPoints.sort()
            for i in range(1, len(critPoints)):
                minima = min(minima, critPoints[i] - critPoints[i - 1])
        else:
            maxima = -1
            minima = -1
        return [minima, maxima]