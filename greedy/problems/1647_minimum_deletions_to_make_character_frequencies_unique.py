# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.

# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

class Solution:
    def minDeletions(self, s: str) -> int:
        count = collections.Counter(s)
        seen = set()
        deletions = 0
        for c in count.values():
            if c not in seen:
                seen.add(c)
            else:
                curr = c
                while curr > 0 and curr in seen:
                    curr -= 1
                    deletions += 1
                seen.add(curr)
        return deletions


