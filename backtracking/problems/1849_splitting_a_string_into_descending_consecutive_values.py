# You are given a string s that consists of only digits.

# Check if we can split s into two or more non-empty substrings such that the numerical values of the substrings are in descending order and the difference between numerical values of every two adjacent substrings is equal to 1.

# For example, the string s = "0090089" can be split into ["0090", "089"] with numerical values [90,89]. The values are in descending order and adjacent values differ by 1, so this way is valid.
# Another example, the string s = "001" can be split into ["0", "01"], ["00", "1"], or ["0", "0", "1"]. However all the ways are invalid because they have numerical values [0,1], [0,1], and [0,0,1] respectively, all of which are not in descending order.
# Return true if it is possible to split s​​​​​​ as described above, or false otherwise.

# A substring is a contiguous sequence of characters in a string.

class Solution:
    def splitString(self, s: str) -> bool:
        N = len(s)
        self.ans = []
        def backtrack(i, path, curr):
            if len(path) > 1 and (int(path[-2]) - int(path[-1])) != 1:
                return False

            if i == N:
                if len(path) > 1:
                    currLen = 0
                    for i in range(len(path)):
                        currLen += len(path[i])
                    return currLen == N
                else:
                    return False
            

            return backtrack(i + 1, path + [curr + s[i]], "") or backtrack(i + 1, path, curr + s[i])
            
        return backtrack(0, [], "")