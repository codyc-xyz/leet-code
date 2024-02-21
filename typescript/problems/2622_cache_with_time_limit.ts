// Write a class that allows getting and setting key-value pairs, however a time until expiration is associated with each key.

// The class has three public methods:

// set(key, value, duration): accepts an integer key, an integer value, and a duration in milliseconds. Once the duration has elapsed, the key should be inaccessible. The method should return true if the same un-expired key already exists and false otherwise. Both the value and duration should be overwritten if the key already exists.

// get(key): if an un-expired key exists, it should return the associated value. Otherwise it should return -1.

// count(): returns the count of un-expired keys.

class TimeLimitedCache {
    private cache: Record<string, number|boolean>;
    private countKeys: number;
    private timeOutIds: Record<string, any>;
    constructor() {
        this.cache = {};
        this.timeOutIds = {};
        this.countKeys = 0;
        
    }
    
    set(key: number, value: number, duration: number): boolean {
        if (key in this.cache && this.cache[key] != false) {
            this.cache[key] = value;
            clearTimeout(this.timeOutIds[key]);
            this.timeOutIds[key] = setTimeout(() => {
                this.cache[key] = false;
                this.countKeys -= 1;
            }, duration)
            return true
        }
        else {
            this.countKeys += 1;
            this.cache[key] = value;
            this.timeOutIds[key] = setTimeout(() => {
                this.cache[key] = false
                this.countKeys -= 1;
            }, duration)
            return false
        }

    }
    
    get(key: number): number|boolean {
        if (key in this.cache && this.cache[key] !== false) {
            return this.cache[key];
        }
        else {
            return -1;
        }
    }
    
    count(): number {
        return this.countKeys;
    }
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */