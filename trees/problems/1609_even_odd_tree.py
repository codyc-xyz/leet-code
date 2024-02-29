# A binary tree is named Even-Odd if it meets the following conditions:

# The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
# For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
# For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
# Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        dq = deque([root])
        depth = 0
        while dq:
            lenDq = len(dq)
            prev = None
            for i in range(lenDq):
                node = dq.popleft()
                if not depth % 2:
                    if not node.val % 2:
                        return False
                    if prev and prev >= node.val:
                        return False
                else:
                    if node.val % 2:
                        return False
                    if prev and prev <= node.val:
                        return False
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
                prev = node.val
            depth += 1
        return True
    

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:


        dq = deque(([root]))
        level = 0
        while dq:
            lenDq = len(dq)
            prev = float('inf') if level % 2 else float('-inf')
            
            while lenDq:
                curr = dq.popleft()
                if level % 2:
                    if curr.val % 2 or curr.val >= prev:
                        return False
                else:
                    if not curr.val % 2 or curr.val <= prev:
                        return False
                prev = curr.val
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
                lenDq -= 1
            level += 1
        return True


