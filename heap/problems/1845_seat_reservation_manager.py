# Design a system that manages the reservation state of n seats that are numbered from 1 to n.

# Implement the SeatManager class:

# SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
# int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
# void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.

class SeatManager:

    def __init__(self, n: int):
        self.heap = [i for i in range(1, n + 1)]
        heapq.heapify(self.heap)

    def reserve(self) -> int:
        return heapq.heappop(self.heap)
        
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)