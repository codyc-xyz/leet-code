# You are given a string s. Reorder the string using the following algorithm:

# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

# Return the result string after sorting s with this algorithm.

class Solution:
    def sortString(self, s: str) -> str:
        ans = ""
        count = collections.Counter(s)
        chars = []
        finished = set()
        seen = set()
        for c in count:
            if c not in seen:
                chars.append(c)
                seen.add(c)

        chars.sort()

        while len(count) > 0:
            for c in chars:
                if c in count:
                    ans += c
                    count[c] -= 1
                    if count[c] == 0:
                        del count[c]
            for c in chars[::-1]:
                if c in count:
                    ans += c
                    count[c] -= 1
                    if count[c] == 0:
                        del count[c]
        return ans


