# Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        j = 0
        stack = []
        
        for n in pushed:
            stack.append(n)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return not stack