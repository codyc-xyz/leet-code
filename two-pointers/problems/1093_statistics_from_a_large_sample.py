# You are given a large sample of integers in the range [0, 255]. Since the sample is so large, it is represented by an array count where count[k] is the number of times that k appears in the sample.

# Calculate the following statistics:
# minimum: The minimum element in the sample.
# maximum: The maximum element in the sample.
# mean: The average of the sample, calculated as the total sum of all elements divided by the total number of elements.
# median:
  # If the sample has an odd number of elements, then the median is the middle element once the sample is sorted.
  # If the sample has an even number of elements, then the median is the average of the two middle elements once the sample is sorted.
# mode: The number that appears the most in the sample. It is guaranteed to be unique.

# Return the statistics of the sample as an array of floating-point numbers [minimum, maximum, mean, median, mode]. Answers within 10-5 of the actual answer will be accepted.

class Solution:
    def sampleStats(self, nums: List[int]) -> List[float]:
        res = count = 0
        smallest = None
        most = 0
        mode = None
        arr = []
        for n, c in enumerate(nums):
            if c > 0:
                if smallest == None:
                    smallest = float(n)
                largest = float(n)
                res += n * c
                count += c
            if c > most:
                most = c
                mode = float(n)
       
        for i in range(255):
            nums[i + 1] += nums[i]
        
        if count % 2 != 0:
            median = bisect.bisect(nums, count / 2)
        else:
            median1 = bisect.bisect(nums, (count - 1) / 2)
            median2 = bisect.bisect(nums, count / 2)
            median = float((median1 + median2) / 2)
        
        return [smallest, largest, res / count, median, mode]
        