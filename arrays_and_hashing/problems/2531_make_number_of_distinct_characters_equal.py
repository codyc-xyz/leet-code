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
