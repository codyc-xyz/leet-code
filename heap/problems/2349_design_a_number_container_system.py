# Design a number container system that can do the following:

# Insert or Replace a number at the given index in the system.
# Return the smallest index for the given number in the system.
# Implement the NumberContainers class:
# NumberContainers() Initializes the number container system.
# void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
# int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.

class NumberContainers:

    def __init__(self):
        self.hm = {}
        self.numberContainers = defaultdict(list)
        
    def change(self, index: int, number: int) -> None:
        self.hm[index] = number
        heapq.heappush(self.numberContainers[number], index)
        
    def find(self, number: int) -> int:
        while self.numberContainers[number] and number != self.hm[self.numberContainers[number][0]]:
            heapq.heappop(self.numberContainers[number])
        if self.numberContainers[number]:
            return self.numberContainers[number][0]
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)