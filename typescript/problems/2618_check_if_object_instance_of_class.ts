// Write a function that checks if a given value is an instance of a given class or superclass. For this problem, an object is considered an instance of a given class if that object has access to that class's methods.

// There are no constraints on the data types that can be passed to the function. For example, the value or the class could be undefined.

function checkIfInstanceOf(obj: any, classFunction: any): boolean {
    if (obj === null || obj === undefined || !classFunction) {
        return false;
    }
    let constructor: any = obj.constructor;

    while (constructor) {
        if (constructor === classFunction) {
            return true
        }
        constructor = Object.getPrototypeOf(constructor.prototype)?.constructor;
    }
    return false
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */