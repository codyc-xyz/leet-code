# Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

# Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
# Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
# The prefix and the suffix should not intersect at any index.
# The characters from the prefix and suffix must be the same.
# Delete both the prefix and the suffix.

# Return the minimum length of s after performing the above operation any number of times (possibly zero times).

class Solution:
    def minimumLength(self, s: str) -> int:
        length = len(s)
        left, right = 0, length - 1

        while right > left:
            removals = 2
            while right - 1 > left and s[right] == s[right - 1]:
                right -= 1
                removals += 1
            while right > left + 1 and s[left] == s[left + 1]:
                left += 1
                removals += 1
            if s[right] == s[left]:
                length -= removals
                right -= 1
                left += 1
            else:
                break
        return length