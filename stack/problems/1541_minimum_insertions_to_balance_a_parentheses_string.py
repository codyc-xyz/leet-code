# Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:
# Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
# Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.

# In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.
# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.

# You can insert the characters '(' and ')' at any position of the string to balance it if needed.

# Return the minimum number of insertions needed to make s balanced.

class Solution:
    def minInsertions(self, s: str) -> int:
        
        stack = []
        i = ans = 0
        
        while i < len(s):
            
            c = s[i]
            
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack:
                    stack.append('(')
                    ans += 1
                if i < len(s) - 1 and s[i+1] == ')':
                    stack.pop()
                    i += 1
                else:
                    ans += 1
                    stack.pop()
            i += 1
            
        return ans + len(stack) * 2