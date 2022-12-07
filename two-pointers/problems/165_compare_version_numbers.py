# Given two version numbers, version1 and version2, compare them.

# Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. 
# Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

# To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. 
# This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. 
# For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

# Return the following:
# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        i = a = b = 0
        
        split1 = version1.split(".")
        split2 = version2.split(".")
    
        while i < len(split1) and i < len(split2):
            if int(split1[i]) > int(split2[i]):
                return 1
            elif int(split1[i]) < int(split2[i]):
                return -1
            i += 1
        while i < len(split1):
            if int(split1[i]) > 0:
                return 1
            i += 1
        while i < len(split2):
            if int(split2[i]) > 0:
                return -1
            i += 1
        return 0