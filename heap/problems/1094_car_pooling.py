# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

# You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        pickups = [(x[1], i) for i, x in enumerate(trips)]
        dropoffs = [(x[2], i) for i, x in enumerate(trips)]
        heapq.heapify(pickups)
        heapq.heapify(dropoffs)
        while pickups:

            while pickups and pickups[0][0] < dropoffs[0][0]:
                _, idx = heapq.heappop(pickups)
                capacity -= trips[idx][0]
                if capacity < 0:
                    return False
            while dropoffs and pickups and dropoffs[0][0] <= pickups[0][0]:
                _, idx = heapq.heappop(dropoffs)
                capacity += trips[idx][0]

        return True
        