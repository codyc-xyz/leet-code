# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr1, arr2 = [], []
        def dfs(root, bias):
            if not root:
                return
            dfs(root.left, bias)
            arr1.append(root.val) if bias else arr2.append(root.val)
            dfs(root.right, bias)
        dfs(root1, True)
        dfs(root2, False)

        ans = []
        i = j = 0
        while i < len(arr1) or j < len(arr2):
            if i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    ans.append(arr1[i])
                    i += 1
                else:
                    ans.append(arr2[j])
                    j += 1
            elif i < len(arr1):
                ans.append(arr1[i])
                i += 1
            elif j < len(arr2):
                ans.append(arr2[j])
                j += 1
        return ans