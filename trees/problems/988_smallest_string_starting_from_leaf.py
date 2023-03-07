# You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

# Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

# As a reminder, any shorter prefix of a string is lexicographically smaller.

# For example, "ab" is lexicographically smaller than "aba".
# A leaf of a node is a node that has no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        self.ans = [99]

        def dfs(root, path):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                curr = path[::-1]
                for i in range(len(self.ans)):
                    if i < len(curr):
                        if self.ans[i] > curr[i]:
                            self.ans = curr
                            break
                        elif self.ans[i] == curr[i]:
                            continue
                        else:
                            break
                    else:
                        self.ans = curr
                        break
                
            dfs(root.left, path[:])
            dfs(root.right, path[:])
        dfs(root, [])
        res = ""
        for n in self.ans:
            res += (chr(ord('a') + n))
                
        return res