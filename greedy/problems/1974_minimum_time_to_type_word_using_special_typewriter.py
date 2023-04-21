# There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer. A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'.

class Solution:
    def minTimeToType(self, word: str) -> int:
        seconds = 0
        i = 0
        prev = 'a'
        while i < len(word):
            curr = abs(ord(prev) - ord(word[i]))
            seconds += min(curr, 26 - curr) + 1
            prev = word[i]
            i += 1
        return seconds

