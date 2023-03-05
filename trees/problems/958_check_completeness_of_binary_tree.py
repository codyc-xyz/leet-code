# Given the root of a binary tree, determine if it is a complete binary tree.

# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        dq = deque([root])
        level = prevLevel = 0
        while dq:
            if prevLevel and level and level // prevLevel != 2:
                return False
            prevLevel = level
            lenDq = len(dq)
            flag = False
            level = 0
            for i in range(len(dq)):
                level += 1
                node = dq.popleft()
                if node.left and flag == False:
                    dq.append(node.left)
                elif node.left:
                    return False
                else:
                    flag = True
                if node.right and flag == False:
                    dq.append(node.right)
                elif node.right:
                    return False
                else:
                    flag = True
            
        return True