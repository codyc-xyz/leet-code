# You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

# If isLefti == 1, then childi is the left child of parenti.
# If isLefti == 0, then childi is the right child of parenti.
# Construct the binary tree described by descriptions and return its root.

# The test cases will be generated such that the binary tree is valid.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hm = {}
        parents = {}
        while descriptions:
            parent, child, side = descriptions.pop()

            if parent not in hm:
                hm[parent] = TreeNode(parent)
            if child not in hm:
                hm[child] = TreeNode(child)
            if side == 1:
                hm[parent].left = hm[child]
            else:
                hm[parent].right = hm[child]
            parents[hm[child]] = hm[parent]

        curr = parents[hm[child]]
        while curr in parents:
            curr = parents[curr]
        return curr