# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s) - 1
        c = list(s)
        while right > left:
            while left < len(s) - 1 and s[left].isalpha() == False:
                left += 1
            while right > 0 and s[right].isalpha() == False:
                right -= 1
            if left < right and s[left].isalpha() and s[right].isalpha():
                tmp = s[left]
                c[left] = c[right]
                c[right] = tmp
                left += 1
                right -= 1
        return "".join(str(x) for x in c)
            