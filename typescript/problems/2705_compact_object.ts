// Given an object or array obj, return a compact object. A compact object is the same as the original object, except with keys containing falsy values removed. This operation applies to the object and any nested objects. Arrays are considered objects where the indices are keys. A value is considered falsy when Boolean(value) returns false.

// You may assume the obj is the output of JSON.parse. In other words, it is valid JSON.

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function compactObject(obj: Obj): Obj {
    let ans: Obj;
    if (Array.isArray(obj)) {
        ans = [];
        for (const item of obj) {
            if ((Array.isArray(item) || typeof item === "object") && Boolean(item) === true) {
                ans.push(compactObject(item))
            }
            else if (Boolean(item) === true) {
                ans.push(item);
            }
        }
    }
    else {
        ans = {}
        Object.keys(obj).forEach(key => {
            const val = obj[key];
            if ((Array.isArray(val) || typeof val === "object") && Boolean(val) === true) {
                ans[key] = compactObject(val);
            }
            else if (Boolean(val) === true) {
                ans[key] = val;
            }
        })
    }

    return ans

}