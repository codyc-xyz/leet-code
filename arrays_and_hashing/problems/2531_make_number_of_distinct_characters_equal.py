# You are given two 0-indexed strings word1 and word2.

# A move consists of choosing two indices i and j such that 0 <= i < word1.length and 0 <= j < word2.length and swapping word1[i] with word2[j].

# Return true if it is possible to get the number of distinct characters in word1 and word2 to be equal with exactly one move. Return false otherwise.

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        
        count1 = [0 for _ in range(26)]
        count2 = [0 for _ in range(26)]

        for c1 in word1:
            count1[ord(c1) - ord('a')] += 1

        for c2 in word2:
            count2[ord(c2) - ord('a')] += 1

        for i in range(26):
            for j in range(26):
                if count1[i] and count2[j]:
                    count1[i] -= 1
                    count2[i] += 1
                    count2[j] -= 1
                    count1[j] += 1
                    res1=res2=0
                    for k in range(26):
                        if count1[k]:
                            res1+=1
                        if count2[k]:
                            res2+=1
                    if res1==res2:
                        return True
                    count1[i] += 1
                    count1[j] -= 1
                    count2[j] += 1
                    count2[i] -= 1
        return False

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        
        count1 = collections.Counter(word1)
        count2 = collections.Counter(word2)
        c1k = list(count1.keys())
        c2k = list(count2.keys())
        for c1 in c1k:
            for c2 in c2k:
                count1[c1] -= 1
                count2[c1] += 1
                count2[c2] -= 1
                count1[c2] += 1
                if not count1[c1]:
                    del count1[c1]
                if not count2[c2]:
                    del count2[c2]
                if len(count1) == len(count2):
                    return True
                count1[c1] += 1
                count2[c1] -= 1
                count1[c2] -= 1
                count2[c2] += 1
                if not count2[c1]:
                    del count2[c1]
                if not count1[c2]:
                    del count1[c2]

        return False
