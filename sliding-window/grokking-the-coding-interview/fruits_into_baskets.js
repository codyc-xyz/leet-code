// Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit
// You can start with any tree, but once you have started you can't skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type
// Write a function to return the maximum number of fruits in both the baskets

function fruits_into_baskets(arr) {
  let windowStart = 0
  let mostFruits = 0
  let substring = []
  for(let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
    while (substring.filter(onlyUnique).length < 2) {
      substring += arr[windowEnd]
      windowEnd += 1
    }
    mostFruits = math.Max(mostFruits, substring.length)
    substring -= arr[windowStart]
    windowStart += 1
  }
  return mostFruits
}

function onlyUnique(value, index, self) {
  return self.indexOf(value) === index;
}