# You are given a string s and two integers x and y. You can perform two types of operations any number of times.

# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score = 0
        stack = []

        if x > y:
            for c in s:
                stack.append(c)
                while len(stack) >= 2:
                    if stack[-2] == 'a' and stack[-1] == 'b':
                        score += x
                        stack.pop()
                        stack.pop()
                    else:
                        break
        else:
            for c in s:
                stack.append(c)
                while len(stack) >= 2:
                    if stack[-2] == 'b' and stack[-1] == 'a':
                        score += y
                        stack.pop()
                        stack.pop()
                    else:
                        break
        
        stack2 = []
        for c in stack:
            stack2.append(c)
            while len(stack2) >= 2:
                if stack2[-2] == 'a' and stack2[-1] == 'b':
                    stack2.pop()
                    stack2.pop()
                    score += x
                elif stack2[-2] == 'b' and stack2[-1] == 'a':
                    stack2.pop()
                    stack2.pop()
                    score += y
                else:
                    break
        return score 

