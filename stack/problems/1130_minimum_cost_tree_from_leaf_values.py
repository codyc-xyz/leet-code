# Given an array arr of positive integers, consider all binary trees such that:

# Each node has either 0 or 2 children
# The values of arr correspond to the values of each leaf in an in -order traversal of the tree.
# The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
# Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

# A node is a leaf if and only if it has zero children.

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [float('inf')]

        for n in arr:
            while stack[-1] <= n:
                mid = stack.pop()
                res += mid * min(stack[-1], n)
            stack.append(n)

        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res
