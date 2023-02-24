# Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

# For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
# Return the root of the reversed tree.
 
# A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

# The level of a node is the number of edges along the path between it and the root node.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        dq = deque([(root, 0)])
        levels = []
        while dq:
            lenDq = len(dq)
            res = []
            for i in range(lenDq):
                node, level = dq.popleft()
                res.append(node)
                if node.left:
                    dq.append((node.left, level + 1))
                    dq.append((node.right, level + 1))
            levels.append(res)
            
        for i, l in enumerate(levels):
            if i % 2:
                for j in range(len(l) // 2):
                    print(l[j].val, l[-j-1].val)
                    l[j].val, l[-j - 1].val = l[-j - 1].val, l[j].val
        return root