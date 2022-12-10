# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
                    
        i = len(nums) - 1
                    
        while i - 1 >= 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            return -1
                    
        j = i
                    
        while j + 1 < len(nums) and nums[j + 1] > nums[i - 1]:
            j += 1
                    
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                    
        nums[i:] = nums[i:][::-1]
                
        res = int("".join(nums))
                    
        if res < 1<<31:
            return res
        else:
            return -1