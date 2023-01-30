# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

class MyHashMap:

    def __init__(self):
        self.arr = []
        self.keys = []
    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.arr.append([key, value])
            self.keys.append(key)
        else:
            for i in range(len(self.arr)):
                if self.arr[i][0] == key:
                    self.arr[i][1] = value

    def get(self, key: int) -> int:
        if key in self.keys:
            for i in range(len(self.arr)):
                    if self.arr[i][0] == key:
                        return self.arr[i][1]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.keys:
            for i in range(len(self.arr)):
                if self.arr[i][0] == key:
                    self.arr.pop(i)
                    self.keys.pop(i)
                    break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)