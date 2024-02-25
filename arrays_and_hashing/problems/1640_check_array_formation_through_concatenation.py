# You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

# Return true if it is possible to form the array arr from pieces. Otherwise, return false.

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
        complete = [False for _ in range(len(arr))]
        
        i = 0
        while i < len(pieces):
            if len(pieces[i]) > 1:
                for j in range(len(arr) - len(pieces[i]) + 1):
                    for k in range(j+len(pieces[i]) - 1, len(arr) + 1):
                        if arr[j:k] == pieces[i]:
                            for q in range(j, k):
                                complete[q] = True

            else:
                if pieces[i][0] in arr:
                    idx = arr.index(pieces[i][0])
                    complete[idx] = True
            i += 1
        return all(complete) == True