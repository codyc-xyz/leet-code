# Given a string s of lower and upper case English letters.

# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

# 0 <= i <= s.length - 2
# 0 <= i <= s.length - 2

# To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

# Notice that an empty string is also good.

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            if (len(stack) > 1): 
                while (stack[-2].islower() and stack[-2].upper() == stack[-1]) or (stack[-2].isupper() and stack[-2].lower() == stack[-1]):
                    stack.pop()
                    stack.pop()
                    if len(stack) < 2:
                        break
        return "".join(stack)