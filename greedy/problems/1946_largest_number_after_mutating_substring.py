# You are given a string num, which represents a large integer. You are also given a 0-indexed integer array change of length 10 that maps each digit 0-9 to another digit. More formally, digit d maps to digit change[d].

# You may choose to mutate a single substring of num. To mutate a substring, replace each digit num[i] with the digit it maps to in change (i.e. replace num[i] with change[num[i]]).

# Return a string representing the largest possible integer after mutating (or choosing not to) a single substring of num.

# A substring is a contiguous sequence of characters within the string.

class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        ans = ""
        i = 0
        while i < len(num):
            if change[int(num[i])] > int(num[i]):
                while change[int(num[i])] >= int(num[i]):
                    ans += str(change[int(num[i])])
                    if i == len(num) - 1:
                        return ans 
                    if change[int(num[i + 1])] < int(num[i + 1]):
                        return ans + num[i + 1:]
                    i += 1
            ans += num[i]
            i += 1
        return ans