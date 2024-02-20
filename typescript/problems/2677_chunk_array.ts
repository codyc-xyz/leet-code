// Given an array arr and a chunk size size, return a chunked array. A chunked array contains the original elements in arr, but consists of subarrays each of length size. The length of the last subarray may be less than size if arr.length is not evenly divisible by size.

// You may assume the array is the output of JSON.parse. In other words, it is valid JSON.

// Please solve it without using lodash's _.chunk function.

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
    let ans: Obj[][] = [];
    let j = 0
    while (j < arr.length) {
        ans.push([])
        for (let i = 0; i < size; i++) {
            if (j+i < arr.length) {
                ans[ans.length-1].push(arr[j+i])
            }
        }
        j += size
    }
    return ans
};
