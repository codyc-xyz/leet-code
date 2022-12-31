# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

# The following rules define a valid string:
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
  
        for i, n in enumerate(s):
            if n == '(':
                stack.append(i)
            elif n == ')':
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                star.append(i)
        
        if not stack:
            return True
        elif star:
            while star and stack and star[-1] > stack[-1]:
                star.pop()
                stack.pop()
            if stack:
                return False
            return True
        else:
            return False