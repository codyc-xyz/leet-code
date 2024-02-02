# You are given a string num representing a large integer. An integer is good if it meets the following conditions:

# It is a substring of num with length 3.
# It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no such integer exists.

# Note:

# A substring is a contiguous sequence of characters within a string.
# There may be leading zeroes in num or a good integer.

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        maxNum = float('-inf')
        count = 1
        prev = num[0]
        for i in range(1, len(num)):
            if num[i] == prev:
                count += 1 
            else:
                count = 1       
            if count == 3:
                maxNum = max(maxNum, int(prev))
                count = 0
            prev = num[i]
        return str(maxNum) * 3 if maxNum > float('-inf') else ""
