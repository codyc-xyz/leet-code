# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. 
# Do the above modifications to the input array in place and do not return anything.

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        queue = deque()
        for i in range(len(arr)):
            queue.append(arr[i])
            if arr[i] == 0:
                queue.append(arr[i])
            arr[i] = queue.popleft()