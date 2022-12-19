# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        
        dq = deque()
    
        for c in s:
            if c == '(' or c == '{' or c == '[':
                dq.append(c)
            elif c == '}':
                if not dq or dq[-1] != '{':
                    return False
                else:
                    dq.pop()
            elif c == ')':
                if not dq or dq[-1] != '(':
                    return False
                else:
                    dq.pop()
            elif c == ']':
                if not dq or dq[-1] != '[':
                    return False
                else:
                    dq.pop()
        return len(dq) == 0