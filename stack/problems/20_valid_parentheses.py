# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        
        opens = {'(', '{', '['}
        stack = []
        
        for i, c in enumerate(s):
            if c in opens:
                stack.append(c)
            else:
                if c == ')':
                    if not stack or stack.pop() != '(':
                        return False
                elif c == '}':
                    if not stack or stack.pop() != '{':
                        return False
                elif c == ']':
                    if not stack or stack.pop() != '[':
                        return False
        return not stack