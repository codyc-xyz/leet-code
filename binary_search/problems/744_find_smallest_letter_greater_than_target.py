# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = ord(target) + 1
        end = ord('z') + 1
        
        for i in range(start, end):
            if chr(i) in letters:
                return chr(i)
        return letters[0]