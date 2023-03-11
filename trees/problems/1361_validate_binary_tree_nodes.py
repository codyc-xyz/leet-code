# You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

# If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

# Note that the nodes have no values and that we only use the node numbers in this problem.

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        children = set(leftChild + rightChild)
        root = -1
        for i in range(n):
            if i not in children and root == -1:
                root = i
            elif i not in children:
                return False
        seen = set()
        dq = deque([root])
        while dq:
            node = dq.popleft()
            if node in seen:
                return False
            if leftChild[node] != -1:
                dq.append(leftChild[node])
            if rightChild[node] != -1:
                dq.append(rightChild[node])
            seen.add(node)
        return len(seen) == n