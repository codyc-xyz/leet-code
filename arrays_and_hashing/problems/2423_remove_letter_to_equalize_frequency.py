# You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

# Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

# Note:

# The frequency of a letter x is the number of times it occurs in the string.
# You must remove exactly one letter and cannot choose to do nothing.

class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        count = collections.Counter(word)
        tmp = count.copy()
        
        for c in count:
            tmp[c] -= 1
            if tmp[c] == 0:
                del tmp[c]
            curr = set(tmp.values())
            if len(curr) == 1:
                return True
            if not tmp[c]:
                tmp[c] = 1
            else:
                tmp[c] += 1
        return False

