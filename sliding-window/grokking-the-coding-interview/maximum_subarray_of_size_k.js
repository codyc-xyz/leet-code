// Given an array of positive numbers and a positive number 'k', find the maximum sum of any contiguous subarray of size 'k'

function find_max_sum_subarray(K, arr) {
  let maxSum = 0
  let windowSum = 0
  let windowStart = 0
  for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
    windowSum += arr[windowEnd];

    if (windowEnd >= K - 1) {
      maxSum = math.Max(windowSum, maxSum)
      windowSum -= arr[windowStart]
      windowStart += 1
    }
  }
  return maxSum
}

find_max_sum_subarray(3, [2, 1, 5, 1, 3, 2])
