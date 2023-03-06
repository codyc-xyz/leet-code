# Given the root of a binary tree and an integer limit, delete all insufficient nodes in the tree simultaneously, and return the root of the resulting binary tree.

# A node is insufficient if every root to leaf path intersecting this node has a sum strictly less than limit.

# A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        
        leafSums = defaultdict(list)
        def dfs(root, currSum):
            if not root:
                return 0
            currSum += root.val
            if not root.left and not root.right:
                leafSums[root].append(currSum)
            l = dfs(root.left, currSum)
            r = dfs(root.right, currSum)
            
            return currSum
        dfs(root, 0)

        remove = set()

        for leaf in leafSums:
            if max(leafSums[leaf]) < limit:
                remove.add(leaf)
        
        for leaf in remove:
            del leafSums[leaf]

        if not leafSums:
            return None
            
        def dfs2(root, prev, left):
            if not root.left and not root.right:
                if root not in leafSums:
                    if left:
                        prev.left = None
                    elif left == False:
                        prev.right = None
                    return False
                else:
                    return True
            l = r = None
            if root.left:
                l = dfs2(root.left, root, True)
            if root.right:
                r = dfs2(root.right, root, False)

            if l or r:
                return True
            else:
                if left:
                    prev.left = None
                else:
                    prev.right = None
            return False
        dfs2(root, None, None)
        return root
