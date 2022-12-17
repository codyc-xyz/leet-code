# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            while len(stack) > 1 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        return "".join(stack)