# You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

# If the character read is a letter, that letter is written onto the tape.
# If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.

# Given an integer k, return the kth letter (1-indexed) in the decoded string.

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if c.isdigit():
                n = len(stack)
                c = int(c)
                while c - 1 > 0:
                    for i in range(n):
                        stack.append(stack[i])
                        if len(stack) > k - 1:
                            return stack[k-1]
                    c -= 1                
            else:
                stack.append(c)
                
        return stack[k - 1]