# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = defaultdict(int)
        singles = {'b', 'a', 'n'}
        doubles = {'o', 'l'}
        for c in text:
            if c in doubles:
                count[c] += 0.5
            elif c in singles:
                count[c] += 1
        if len(count) == 5:
            return int(min(count.values()))
        else:
            return 0