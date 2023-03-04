# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        def dfs(head):
            if not head:
                return None
            if not head.next:
                return TreeNode(head.val)
            fast = slow = head
            prev = ListNode(next=head)
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                prev = prev.next
            prev.next = None
            root = TreeNode(slow.val)
            root.left = dfs(head)
            root.right = dfs(slow.next)
            return root
        return dfs(head)