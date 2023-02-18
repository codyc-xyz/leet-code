# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        arr1 = [root.left] if root.left else []
        arr2 = [root.right] if root.right else []
        while arr1 or arr2:
            if not arr1 or not arr2 or arr1[-1].val != arr2[-1].val:
                return False
            node1, node2 = arr1.pop(), arr2.pop()
            if node1.left and node2.right and node1.left.val == node2.right.val:
                arr1.append(node1.left)
                arr2.append(node2.right)
            elif node1.left or node2.right:
                return False
            if node1.right and node2.left and node1.right.val == node2.left.val:
                arr1.append(node1.right)
                arr2.append(node2.left)
            elif node1.right or node2.left:
                return False
        return True

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        arr1, arr2 = [], []
        def bfs(node, bias):
            if not node:
                if bias:
                    arr1.append(None)
                else:
                    arr2.append(None)
                return
            if bias:
                arr1.append(node.val)
                bfs(node.left, bias)
                bfs(node.right, bias)
            else:
                arr2.append(node.val)
                bfs(node.right, bias)
                bfs(node.left, bias)
        bfs(root.left, True)
        bfs(root.right, False)
        return arr1 == arr2
