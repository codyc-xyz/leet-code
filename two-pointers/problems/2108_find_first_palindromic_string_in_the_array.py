# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        palindromic = ""
        
        for word in words:
            right = len(word) - 1
            left = 0
            count = 0
            while right > left:
                if word[right] == word[left]:
                    right -= 1
                    left += 1
                    count += 1
                    continue
                else:
                    break
            if count == len(word) // 2:
                palindromic += word
                break
        return palindromic