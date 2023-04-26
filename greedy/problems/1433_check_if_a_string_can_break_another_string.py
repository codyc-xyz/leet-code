# Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa. In other words s2 can break s1 or vice-versa.

# A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:

        s1 = sorted(s1)
        s2 = sorted(s2)
        if s1[0] > s2[0]:
            for i in range(1, len(s1)):
                if s2[i] > s1[i]:
                    return False
        elif s2[0] > s1[0]:
            for i in range(1, len(s1)):
                if s1[i] > s2[i]:
                    return False
        else:
            flag = True
            for i in range(1, len(s1)):
                if s2[i] > s1[i]:
                    flag = False
                    break
            if flag == True:
                return True
            for i in range(1, len(s1)):
                if s1[i] > s2[i]:
                    return False
                    
        return True