# Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def isPalindromic(path):
            count = {}
            seenOdd = False
            for c in path:
                count[c] = count.get(c, 0) + 1
            for num in count.values():
                if num % 2:
                    if seenOdd:
                        return False
                    seenOdd = True
            return True
        
        def dfs(root, path):
            if not root:
                return
            path.append(root.val)        
            dfs(root.left, path[:])
            dfs(root.right, path[:])
            if not root.left and not root.right:
                if isPalindromic(path):
                    self.ans += 1     
        dfs(root, [])
        return self.ans