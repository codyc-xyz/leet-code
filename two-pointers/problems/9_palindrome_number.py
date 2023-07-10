# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:

        X = str(x)
        l, r = 0, len(X) - 1

        while l < r:
            if X[l] != X[r]:
                return False
            l += 1
            r -= 1
        return True