# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ""
        opened = 0
        for c in s:
            if c == '[':
                opened += 1
            elif opened == 0 and c.isalpha() == True:
                ans += c
            if c != ']':
                stack.append(c)
            else:
                num = ""
                string = ""
                opened -= 1
                while stack[-1].isalpha() == True:
                    string += stack.pop()
                stack.pop()
                while stack and stack[-1].isnumeric() == True:
                    num += stack.pop()
                num = num[::-1]
                if opened > 0:
                    for i in range(int(num)):
                        for c in string:
                            stack.append(c)
                else:
                    string = string[::-1]
                    ans += int(num) * string
        return ans