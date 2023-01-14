# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
# If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

class TimeMap:

    def __init__(self):
        self.tMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tMap:
            self.tMap[key] = [[value, timestamp]]
        else:
            self.tMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        vals = self.tMap.get(key, [])
        l, r = 0, len(vals) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if vals[m][1] <= timestamp:
                ans = vals[m][0]
                l = m + 1
            else:
                r = m - 1
        return ans
            

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)