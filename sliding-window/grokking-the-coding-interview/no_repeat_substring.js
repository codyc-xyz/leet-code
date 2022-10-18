// Given a string, find the length of the longest substring which has no repeating characters.

function no_repeat_substring(string) {
  let arr = string.split('')
  let windowStart = 0
  let substring = []
  let longestSubstring = 0
  for(let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
    while (substring[windowEnd] !== substring[windowEnd - 1]) {
      substring += arr[windowEnd]
      windowEnd += 1
    }
    longestSubstring = math.Max(longestSubstring, substring.length)
    substring -= arr[windowStart]
    windowStart += 1
  }
  return longestSubstring
}
