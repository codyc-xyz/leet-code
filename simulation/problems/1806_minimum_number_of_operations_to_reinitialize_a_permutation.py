# You are given an even integer n​​​​​​. You initially have a permutation perm of size n​​ where perm[i] == i​ (0-indexed)​​​​.

# In one operation, you will create a new array arr, and for each i:

# If i % 2 == 0, then arr[i] = perm[i / 2].
# If i % 2 == 1, then arr[i] = perm[n / 2 + (i - 1) / 2].
# You will then assign arr​​​​ to perm.

# Return the minimum non-zero number of operations you need to perform on perm to return the permutation to its initial value.

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        
        perm = [i for i in range(n)]
        arr = []
        for i, p in enumerate(perm):
            if not p % 2:
                arr.append(perm[i//2])
            else:
                arr.append(perm[n//2 + (i-1) // 2])
        
        ans = 1
        while arr != perm:
            prev_arr = [0] * n
            for i in range(n):
                if not i % 2:
                    prev_arr[i] = arr[i//2]
                else:
                    prev_arr[i] = arr[n//2 + (i-1) // 2]
            ans += 1
            arr = prev_arr

        return ans