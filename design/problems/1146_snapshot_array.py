# Implement a SnapshotArray that supports the following interface:

# SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to val.
# int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
# int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

class SnapshotArray:

    def __init__(self, length: int):
        self.snapArr = [0 for _ in range(length)]
        self.snapshot = {}
        

    def set(self, index: int, val: int) -> None:
        self.snapArr[index] = val
        

    def snap(self) -> int:
        self.snapshot[len(self.snapshot) -1] = self.snapArr[:]
        return len(self.snapshot) - 1
        

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshot[snap_id-1][index]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)