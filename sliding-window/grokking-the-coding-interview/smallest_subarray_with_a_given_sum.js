// Given an array of positive numbers and a positive number 'S', find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. Return 0, if no such subarray exists (EASY)

function find_smallest_subarray_with_given_sum(S, arr) {
  let windowSum = 0
  let windowStart = 0
  let minLength = Math.pow(10, 1000)
  for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
    windowSum += arr[windowEnd];
    while (windowSum >= S) {
      minLength = math.Min(windowEnd - windowStart + 1, minLength)
      windowSum -= arr[windowStart]
      windowStart += 1
    }
  }
  return minLength == Math.pow(10, 1000) ? 0 : minLength
}