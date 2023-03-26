# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Implement KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = sorted(nums)
        self.k = k
        

    def add(self, val: int) -> int:
        i = 0
        while i < len(self.heap) and val > self.heap[i]:
            i += 1
        self.heap.insert(i, val)
        return self.heap[-self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)