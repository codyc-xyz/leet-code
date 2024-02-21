// Given two arrays arr1 and arr2, return a new array joinedArray. All the objects in each of the two inputs arrays will contain an id field that has an integer value. joinedArray is an array formed by merging arr1 and arr2 based on their id key. The length of joinedArray should be the length of unique values of id. The returned array should be sorted in ascending order based on the id key.

// If a given id exists in one array but not the other, the single object with that id should be included in the result array without modification.

// If two objects share an id, their properties should be merged into a single object:

// If a key only exists in one object, that single key-value pair should be included in the object.
// If a key is included in both objects, the value in the object from arr2 should override the value from arr1.

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type ArrayType = { "id": number } & Record<string, JSONValue>;

function join(arr1: ArrayType[], arr2: ArrayType[]): ArrayType[] {

    let ans: ArrayType[] = [...arr1];

    for (let i = 0; i < arr2.length; i++) {
        let curr: ArrayType = arr2[i];
        let idx = ans.findIndex(item => item.id === curr.id);
        if (idx === -1) {
            ans.push(curr);
        }
        else {
            ans[idx] = {...ans[idx], ...curr}
        }
    }
    return ans.sort((a, b) => a.id - b.id)
};

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type ArrayType = { "id": number } & Record<string, JSONValue>;

function join(arr1: ArrayType[], arr2: ArrayType[]): ArrayType[] {
    let ans: ArrayType[] = [];
    let hm: Object = {};
    for (let i = 0; i < arr1.length; i++) {
        hm[arr1[i].id] = arr1[i]
    }

    for (let i = 0; i < arr2.length; i++) {
        let curr: ArrayType = arr2[i];
        if (curr.id in hm) {
            hm[curr.id] = {...hm[curr.id], ...curr}
        }
        else {
            hm[curr.id] = arr2[i];
        }
    }
    Object.keys(hm).forEach(key => {
        if (hm[key] !== undefined) {
            ans.push(hm[key])
        }
    })
    return ans.sort((a, b) => a.id - b.id);
};