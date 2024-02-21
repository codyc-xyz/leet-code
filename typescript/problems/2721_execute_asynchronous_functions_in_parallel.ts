// Given an array of asynchronous functions functions, return a new promise promise. Each function in the array accepts no arguments and returns a promise. All the promises should be executed in parallel.

// promise resolves:

// When all the promises returned from functions were resolved successfully in parallel. The resolved value of promise should be an array of all the resolved values of promises in the same order as they were in the functions. The promise should resolve when all the asynchronous functions in the array have completed execution in parallel.
// promise rejects:

// When any of the promises returned from functions were rejected. promise should also reject with the reason of the first rejection.
// Please solve it without using the built-in Promise.all function.

type Fn<T> = () => Promise<T>

async function promiseAll<T>(functions: Fn<T>[]): Promise<T[]> {

    return new Promise<T[]> ((resolve, reject) => {
        if (functions.length === 0) {
            resolve([])
            return
        }
        else {
            let ans: T[] = new Array(functions.length).fill(null);
            let count: number = 0;
            functions.forEach(async (item, idx) => {
                try {

                ans[idx] = await item();
                count++
                if (count === functions.length) {
                    resolve(ans);
                    }
                }
                catch(err) {
                reject(err)
                }
            });
        }});
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */