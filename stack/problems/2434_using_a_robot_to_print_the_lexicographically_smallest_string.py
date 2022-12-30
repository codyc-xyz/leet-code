# You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:
# Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
# Remove the last character of a string t and give it to the robot. The robot will write this character on paper.

# Return the lexicographically smallest string that can be written on the paper.

class Solution:
    def robotWithString(self, s: str) -> str:

        t = []
        counter = collections.Counter(s)
        ans = ""
        
        for c in s:
            t.append(c)
            if counter[c] == 1:
                del counter[c]
            else:
                counter[c] -= 1
            
            while counter and t and t[-1] <= min(counter):
                ans += t.pop()
        ans += ''.join(t[::-1])
        
        return ans