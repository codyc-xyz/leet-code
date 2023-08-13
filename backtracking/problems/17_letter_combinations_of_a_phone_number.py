# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hm = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        ans = []
        def backtrack(i, path):
            if i == len(digits):
                ans.append(''.join(path))
                return
    
            for letter in hm[digits[i]]:
                path.append(letter)
                backtrack(i + 1, path[:])
                path.pop()
            
        backtrack(0, [])
        return ans

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hm = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        ans = []
        def backtrack(i, path):
            if i == len(digits):
                ans.append(path)
                return
    
            for letter in hm[digits[i]]:
                backtrack(i + 1, path + letter)
                
        if digits: 
            backtrack(0, "")
        return ans
    

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        N = len(digits)
        self.ans = []
        hm = {
            '2': {'a', 'b', 'c'},
            '3': {'d', 'e', 'f'},
            '4': {'g', 'h', 'i'},
            '5': {'j', 'k', 'l'},
            '6': {'m', 'n', 'o'},
            '7': {'p', 'q', 'r', 's'},
            '8': {'t', 'u', 'v'},
            '9': {'w', 'x', 'y', 'z'}
        }

        def backtrack(i, res):
            if i == N:
                self.ans.append(res)
                return
            for c in hm[digits[i]]:
                backtrack(i + 1, res + c)

        if digits:
            backtrack(0, "")
        return self.ans
