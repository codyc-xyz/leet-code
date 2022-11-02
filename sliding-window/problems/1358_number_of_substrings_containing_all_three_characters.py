# Given a string s consisting only of characters a, b and c.
# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

class Solution:
 
    def numberOfSubstrings(self, s: str) -> int:
        windowStart = count = 0
        a = b = c = 0
        for windowEnd in range(len(s)):
            if s[windowEnd] == 'a':
                a+= 1
            elif s[windowEnd] == 'b':
                b+= 1
            else:
                c += 1
            while a > 0 and b > 0 and c > 0:
                count += len(s) - windowEnd
                if s[windowStart] == 'a':
                    a -= 1
                elif s[windowStart] == 'b':
                    b -= 1
                else:
                    c -= 1
                windowStart += 1
        return count
        
