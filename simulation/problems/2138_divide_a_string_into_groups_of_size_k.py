# A string s can be partitioned into groups of size k using the following procedure:

# The first group consists of the first k characters of the string, the second group consists of the next k characters of the string, and so on. Each character can be a part of exactly one group.
# for the last group, if the string does not have k characters remaining, a character fill is used to complete the group.
# Note that the partition is done so that after removing the fill character from the last group (if it exists) and concatenating all the groups in order, the resultant string should be s.

# Given the string s, the size of each group k and the character fill, return a string array denoting the composition of every group s has been divided into, using the above procedure.

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        ans = []

        for i in range(0, len(s), k):
            ans.append(s[i:i+k])
        while len(ans[-1]) < k:
            ans[-1] += fill
        return ans