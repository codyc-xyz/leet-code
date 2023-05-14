# Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:

        hm = {}

        for n in arr:
            if n in hm:
                hm[n] += 1
            else:
                hm[n] = 1
        arr.sort()
        for val in arr:
            if val in hm and val * 2 in hm:
                if val == 0 and hm[val] < 2:
                    return False
        
                hm[val * 2] -= 1
                if hm[val*2] == 0:
                    del hm[val*2]
                hm[val] -= 1
                if hm[val] == 0:
                    del hm[val]
            elif val in hm and not val % 2 and val // 2 in hm:
                hm[val // 2] -= 1
                if hm[val//2] == 0:
                    del hm[val//2] 
                hm[val] -= 1
                if hm[val] == 0:
                    del hm[val]
        return not hm