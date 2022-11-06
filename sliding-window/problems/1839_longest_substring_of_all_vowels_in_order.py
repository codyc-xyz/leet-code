# A string is considered beautiful if it satisfies the following conditions:
# Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
# The letters must be sorted in alphabetical order 
# (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).

# For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, 
# but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.

# Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. 
# If no such substring exists, return 0.

# A substring is a contiguous sequence of characters in a string.

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        maxCount = count = windowEnd = 0
        if len(word) < 5:
            return 0
        for windowStart in range(len(word)):
            k = windowEnd
            if word[windowEnd] == 'a' and windowEnd < len(word) - 4:
                while word[windowEnd] == 'a' and windowEnd < len(word) - 4: 
                    count += 1
                    windowEnd += 1
                if word[windowEnd] == 'e' and windowEnd < len(word) - 3:
                    while word[windowEnd] == 'e' and windowEnd < len(word) - 3:
                        count += 1
                        windowEnd += 1
                    if word[windowEnd] == 'i' and windowEnd < len(word) - 2:
                        while word[windowEnd] == 'i' and windowEnd < len(word) - 2:
                            count += 1
                            windowEnd += 1
                        if word[windowEnd] == 'o' and windowEnd < len(word) - 1:
                            while word[windowEnd] == 'o' and windowEnd < len(word) - 1:
                                count += 1
                                windowEnd += 1
                            if word[windowEnd] == 'u' and windowEnd < len(word):
                                while windowEnd < len(word) and word[windowEnd] == 'u':
                                    count += 1
                                    windowEnd += 1
                            else:
                                count = 0
                        else:
                            count = 0
                    else:
                        count = 0
                else:
                    count = 0 
            else:
                count = 0
              
            if k == windowEnd:
                windowEnd += 1
            maxCount = max(maxCount, count)
            count = 0
            if windowEnd >= len(word):
                break
        return maxCount
                

