# A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

# Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

# Implement the CBTInserter class:

# CBTInserter(TreeNode root) Initializes the data structure with the root of the complete binary tree.
# int insert(int v) Inserts a TreeNode into the tree with value Node.val == val so that the tree remains complete, and returns the value of the parent of the inserted TreeNode.
# TreeNode get_root() Returns the root node of the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.ans = root
        self.dq = deque([root])
        while True:
            flag = False
            lenDq = len(self.dq)
            for i in range(lenDq):
                node = self.dq[0]
                if node.left and node.right:
                    self.dq.popleft()
                    self.dq.append(node.left)
                    self.dq.append(node.right)
                else: 
                    flag = True
                    if node.left: self.dq.append(node.left)
                    break
            if flag == True:
                break

    def insert(self, val: int) -> int:
        node = TreeNode(val)
        parent = self.dq[0]
        if not self.dq[0].left:
            self.dq[0].left = node
        else:
            self.dq[0].right = node
            self.dq.popleft()
        self.dq.append(node)
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.ans