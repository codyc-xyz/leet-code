# You are given two strings a and b of the same length. Choose an index and split both strings at the same index, 
# splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. 
# Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.

# When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.

# Return true if it is possible to form a palindrome string, otherwise return false.

# Notice that x + y denotes the concatenation of strings x and y.

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.checkChars(a, b) or self.checkChars(b, a)
    
    def checkChars(self, a, b):
        
        l, r = 0, len(a) - 1
        
        while l < r and a[l] == b[r]:
            l += 1
            r -= 1
            
        return self.isPalindrome(a[:l] + b[l:]) or self.isPalindrome(a[:r + 1] + b[r+ 1:])
    
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True