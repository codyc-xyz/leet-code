# You are given an integer num. You know that Danny Mittal will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

# Return the difference between the maximum and minimum values Danny can make by remapping exactly one digit in num.

# Notes:

# When Danny remaps a digit d1 to another digit d2, Danny replaces all occurrences of d1 in num with d2.
# Danny can remap a digit to itself, in which case num does not change.
# Danny can remap different digits for obtaining minimum and maximum values respectively.
# The resulting number after remapping can contain leading zeroes.
 
class Solution:
    def minMaxDifference(self, num: int) -> int:

        nums = list(str(num))
        if nums[0] != '9':
            maxPrev = nums[0]
        else:
            i = 1
            while i < len(nums) and nums[i] == '9':
                i += 1
            if i == len(nums):
                return num 
            maxPrev = nums[i]
        if nums[0] != '0':
            minPrev = nums[0]
        else:
            i = 1
            while i < len(nums) and nums[i] == '0':
                i += 1
            if i == len(nums):
                return num 
            minPrev = nums[i]
        maxNum = ""
        minNum = ""
        for n in (nums):
            if n == maxPrev or n == minPrev:
                if n == maxPrev:
                    maxNum += '9'
                else:
                    maxNum += n
                if n == minPrev:
                    minNum += '0'
                else:
                    minNum += n
                continue
            minNum += n
            maxNum += n
        return int(maxNum) - int(minNum)
