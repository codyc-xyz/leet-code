# You are given two 0-indexed arrays of strings startWords and targetWords. Each string consists of lowercase English letters only.

# For each string in targetWords, check if it is possible to choose a string from startWords and perform a conversion operation on it to be equal to that from targetWords.

# The conversion operation is described in the following two steps:

# Append any lowercase letter that is not present in the string to its end.
# For example, if the string is "abc", the letters 'd', 'e', or 'y' can be added to it, but not 'a'. If 'd' is added, the resulting string will be "abcd".
# Rearrange the letters of the new string in any arbitrary order.
# For example, "abcd" can be rearranged to "acbd", "bacd", "cbda", and so on. Note that it can also be rearranged to "abcd" itself.
# Return the number of strings in targetWords that can be obtained by performing the operations on any string of startWords.

# Note that you will only be verifying if the string in targetWords can be obtained from a string in startWords by performing the operations. The strings in startWords do not actually change during this process.

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        countStart = []
        countTarget = []

        for s in startWords:
            arr = [0 for _ in range(26)]
            for c in s:
                arr[ord(c) - ord('a')] += 1
            countStart.append(arr)

        for t in targetWords:
            arr = [0 for _ in range(26)]
            for c in t:
                arr[ord(c) - ord('a')] += 1
            countTarget.append(arr)
        ans = 0
        for k, t in enumerate(countTarget):
            for l, s in enumerate(countStart):
                diff = len(targetWords[k]) - len(startWords[l])
                if diff != 1:
                    continue
                flag = True
                for i in range(26):
                    if s[i] != t[i] and t[i] > 1 or s[i] and not t[i]:
                        flag = False
                        break
                if flag:
                    ans += 1
                    break
                
        return ans

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        
        start = set([''.join(sorted(s)) for s in startWords])

        ans = 0
        for t in targetWords:
            curr = ''.join(sorted(t))
            for i in range(len(curr)):
                if curr[:i] + curr[i+1:] in start:
                    ans += 1
                    break
        return ans