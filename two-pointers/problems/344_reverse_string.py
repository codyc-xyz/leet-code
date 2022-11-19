# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        right, left = len(s) - 1, 0
        for i in range((len(s) + 1) // 2):
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            right -= 1
            left += 1
        return s
        