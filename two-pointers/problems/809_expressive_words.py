# Sometimes people repeat letters to represent extra feeling. For example:
# "hello" -> "heeellooo"
# "hi" -> "hiiii"

# In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

# You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: 
# choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. 
# Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.

# Return the number of query strings that are stretchy.

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        res = 0
        
        for word in words:
            flag = True
            a = b = 0
            while b < len(s):
                if a >= len(word):
                    flag = False
                    break
                countA = countB = 0
                while b < len(s) and s[b] == word[a]:
                    b += 1
                    countB += 1
                while a < len(word) and b - 1 < len(s) and s[b - 1] == word[a]:
                    a += 1
                    countA += 1
                if (a < len(word) and word[a] not in s) or (b < len(s) and s[b] not in word):
                    flag = False
                    break
                    
                if a < len(word) and b < len(s) and word[a] != s[b]:
                    flag = False
                    break
    
                if countB == countA or (countB > 2 and countB > countA):
                    continue
                else:
                    flag = False
                    break
            if flag == True:
                res += 1
        return res