# Given an array of strings queries and a string pattern, return a boolean array answer where answer[i] is true if queries[i] matches pattern, and false otherwise.

# A query word queries[i] matches pattern if you can insert lowercase English letters pattern so that it equals the query. 
# You may insert each character at any position and you may not insert any characters.

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        ans = []
        flag = 1
        for query in queries:
            if len(pattern) > len(query):
                ans.append(False)
                continue
            queryPointer = patternPointer = 0
            while queryPointer < len(query):
                if patternPointer >= len(pattern) and query[queryPointer] == pattern[patternPointer - 1]:
                    flag = 0
                    break
                elif patternPointer < len(pattern) and query[queryPointer] == pattern[patternPointer]:
                    patternPointer += 1
                elif query[queryPointer].isupper():
                    flag = 0
                    break
                queryPointer += 1
            if flag == 1 and patternPointer == len(pattern):
                ans.append(True)
            else:
                ans.append(False)
            flag = 1
        return ans