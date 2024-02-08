# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if not low % 2:
            return (high-low+1)//2
        return (high-low)//2+1
