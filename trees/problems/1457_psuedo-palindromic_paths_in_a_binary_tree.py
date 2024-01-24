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
            seenOdd = False
            for num in path.values():
                if num % 2:
                    if seenOdd:
                        return False
                    seenOdd = True
            return True
        
        def dfs(root, path):
            if not root:
                return
            path[root.val] += 1
            if not root.left and not root.right:
                if isPalindromic(path):
                    self.ans += 1          
            dfs(root.left, path)
            dfs(root.right, path)
            path[root.val] -= 1
        dfs(root, defaultdict(int))
        return self.ans
    
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, path, count):
            if node.val in count:
                count[node.val] += 1
            else:
                count[node.val] = 1
            if not node.left and not node.right:
                odds = 0
                if len(path) % 2:
                    for c in count:
                        if count[c] % 2:
                            if odds:
                                count[node.val] -= 1
                                return
                            odds += 1
                else:
                    for c in count:
                        if count[c] % 2:
                            count[node.val] -= 1
                            return
                self.ans += 1
            if node.left:
                dfs(node.left, path + [node.left.val], count)
            if node.right:
                dfs(node.right, path + [node.right.val], count)
            count[node.val] -= 1

        dfs(root, [root.val], {})
        return self.ans
            

            

