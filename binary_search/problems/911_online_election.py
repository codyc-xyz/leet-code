# You are given two integer arrays persons and times. In an election, the ith vote was cast for persons[i] at time times[i].

# For each query at a time t, find the person that was leading the election at time t. Votes cast at time t will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

# Implement the TopVotedCandidate class:
# TopVotedCandidate(int[] persons, int[] times) Initializes the object with the persons and times arrays.
# int q(int t) Returns the number of the person that was leading the election at time t according to the mentioned rules.

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        votes = defaultdict(int)
        self.time = [] 
        winning, count = None, 0
        for i in range(len(times)):
            votes[persons[i]] += 1
            if votes[persons[i]] >= count:
                winning = persons[i]
                count = votes[persons[i]]
                self.time.append([times[i], winning])
        self.time_list = [t[0] for t in self.time]
        
    def q(self, t: int) -> int:
        curr = bisect_left(self.time_list, t)
        if curr == len(self.time):
            return self.time[curr - 1][1]
        elif self.time[curr][0] == t:
            return self.time[curr][1]
        else:
            return self.time[curr - 1][1]
        return self.time[curr - 1][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)