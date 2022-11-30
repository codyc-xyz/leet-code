# Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. 
# If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort()
        ans = ""
        
        for word in dictionary:
            a = b = 0
            while b < len(s) and a < len(word):
                if word[a] == s[b]:
                    a += 1
                b += 1
            if a == len(word) and len(word) > len(ans):
                ans = word
        return ans