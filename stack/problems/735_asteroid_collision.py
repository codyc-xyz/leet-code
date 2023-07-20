# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for a in asteroids:
            flag = False
            while stack and stack[-1] >= 0 and a < 0 and flag == False:
                if abs(a) > abs(stack[-1]):
                    stack.pop()
                elif abs(a) < abs(stack[-1]):
                    flag = True
                else:
                    stack.pop()
                    flag = True
            if flag == False:
                stack.append(a)
        return stack
    

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        N = len(asteroids)
        stack = []

        for i in range(N):
            curr = asteroids[i]
            if stack:
                if curr < 0 and stack[-1] > 0:
                    while stack and abs(curr) > stack[-1] and stack[-1] > 0:
                        stack.pop()
                    if stack and stack[-1] == abs(curr):
                        stack.pop()
                        continue
                    elif stack and stack[-1] > abs(curr):
                        continue
            stack.append(curr)
        return stack
