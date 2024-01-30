# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = {'*', '+', '-', '/'}
        
        for i, t in enumerate(tokens):
            if t in operators:
                a = stack.pop()
                b = stack.pop()
                if t == '*':
                    stack.append(int(b * a))
                elif t == '+':
                    stack.append(int(b + a))
                elif t == '-':
                    stack.append(int(b - a))
                else:
                    stack.append(int(b / a))
            else:
                stack.append(int(t))
                
        return stack[-1]
    

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = {'+', '-', '*', '/'}
        stack = []

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                a = stack.pop()
                b = stack.pop()
                if t == '+':
                    curr = b + a
                elif t == '-':
                    curr = b - a
                elif t == '*':
                    curr = b * a
                else:
                    curr = int(b / a)
                stack.append(curr)

        return int(stack[-1])