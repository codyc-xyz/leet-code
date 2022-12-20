# You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

# A 0-indexed string num of length n + 1 is created using the following conditions:
# num consists of the digits '1' to '9', where each digit is used at most once.
# If pattern[i] == 'I', then num[i] < num[i + 1].
# If pattern[i] == 'D', then num[i] > num[i + 1].

# Return the lexicographically smallest possible string num that meets the conditions.

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        stack = [1]
        tmp = []
        i = 2
        ans = ""
        for p in pattern:
            if p == 'I':
                while tmp:
                    stack.append(tmp.pop())
                stack.append(i)
            else:
                tmp.append(stack.pop())
                stack.append(i)
            i += 1
        while tmp:
            stack.append(tmp.pop())
            
        for c in stack:
            ans += str(c)
        return ans