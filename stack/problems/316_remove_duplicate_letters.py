# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        smallest = "zzzzzzzzz"
        stack = deque()
        target = len(set(s))
        
        hm = {}
        
        for i, n in enumerate(s):
            hm[n] = i
            
        for i, c in enumerate(s):
            if c not in stack:
                while stack and c < stack[-1] and hm[stack[-1]] > i:
                    stack.pop()
                stack.append(c)              
            if len(stack) == target:
                smallest = min(smallest, "".join(stack))
                
        return smallest