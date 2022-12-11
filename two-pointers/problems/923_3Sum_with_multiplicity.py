# Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

# As the answer can be very large, return it modulo 109 + 7.

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = 0
        arr.sort()
        for i in range(len(arr) - 2):
            
            l, r = i + 1, len(arr) - 1
            while r > l:
                threeSum = arr[l] + arr[r] + arr[i]
                if threeSum > target:
                    r -= 1
                elif threeSum < target:
                    l += 1
                elif arr[r] != arr[l]:
                    left = right = 1
                    while arr[r] == arr[r - 1]:
                        r -= 1
                        right += 1
                    while arr[l] == arr[l + 1]:
                        l += 1
                        left += 1
                    count += right * left
                    r -= 1
                    l += 1
                else:
                    count += (r - l + 1) * (r-l) / 2
                    break
        return int(count%(10**9 + 7))