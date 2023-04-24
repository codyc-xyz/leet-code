# You are given a string time in the form of  hh:mm, where some of the digits in the string are hidden (represented by ?).

# The valid times are those inclusively between 00:00 and 23:59.

# Return the latest valid time you can get from time by replacing the hidden digits.

class Solution:
    def maximumTime(self, time: str) -> str:
        ans = ""

        for i, c in enumerate(time):
            if c == '?':
                if i == 0:
                    if time[i + 1] != '?' and int(time[i + 1]) >= 4:
                        ans += '1'
                    else:
                        ans += '2'
                elif i == 1:
                    if ans == '2':
                        ans += '3'
                    else:
                        ans += '9'
                elif i == 3:
                    ans += '5'
                else:
                    ans += '9'
            else:
                ans += c

        return ans