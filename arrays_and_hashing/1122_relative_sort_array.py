# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        count1 = collections.Counter(arr1)
        set2 = set(arr2)
        ans = []
        for n in arr2:
            ans += [n] * count1[n]

        seen = set()
        for n in arr1:
            if n not in set2 and n not in seen:
                ans += [n] * count1[n]
                seen.add(n)
        return ans
