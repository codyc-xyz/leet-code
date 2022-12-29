# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

class Solution:
    def calculate(self, s: str) -> int:
        
        num, stack, op = 0, [], "+"
        operators = {'+', '-', '*', '/'}
        for i, c in enumerate(s):
                
            if c.isdigit():
                num = num * 10 + int(c)
            if c in operators or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                op = c
        return sum(stack)