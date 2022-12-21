# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        opens = 0
        for c in s:
            if c == ')' and opens < 1:
                continue
            elif c == ')':
                opens -= 1
            elif c == '(':
                opens += 1
            stack.append(c)
            
        r = len(stack) - 1
        while opens > 0:
            if stack[r] == '(':
                stack.pop(r)
                opens -= 1
            r -= 1 
        
        return "".join(stack)