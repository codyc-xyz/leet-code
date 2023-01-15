# Let the function f(s) be the frequency of the lexicographically smallest character in a non-empty string s. 
# For example, if s = "dcce" then f(s) = 2 because the lexicographically smallest character is 'c', which has a frequency of 2.

# You are given an array of strings words and another array of query strings queries. For each query queries[i], count the number of words in words such that f(queries[i]) < f(W) for each W in words.

# Return an integer array answer, where each answer[i] is the answer to the ith query.

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans = []
        arr = []
        for w in words:
            count = 0
            smallestChar = min(w)
            for c in range(len(w)):
                if w[c] == smallestChar:
                    count += 1
            arr.append(count)
        arr.sort()
        
        for q in queries:
            count = 0
            smallestChar = min(q)
            for c in range(len(q)):
                if q[c] == smallestChar:
                    count += 1
            ans.append(len(arr) - bisect_right(arr, count))
        return ans