# Given a binary tree with the following rules:

# root.val == 0
# If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
# If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
# Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

# Implement the FindElements class:

# FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
# bool find(int target) Returns true if the target value exists in the recovered binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.vals = set()
        def dfs(root, prev, bias):
            if not root:
                return
            if bias == True:
                root.val = prev * 2 + 1
            elif bias == False:
                root.val = prev * 2 + 2
            else:
                root.val = 0
            self.vals.add(root.val)
            dfs(root.left, root.val, True)
            dfs(root.right, root.val, False)
        dfs(root, 0, None)


    def find(self, target: int) -> bool:
        if target in self.vals:
            return True
        else:
            return False