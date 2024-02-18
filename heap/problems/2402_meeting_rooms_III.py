# You are given an integer n. There are n rooms numbered from 0 to n - 1.

# You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

# Meetings are allocated to rooms in the following manner:

# Each meeting will take place in the unused room with the lowest number.
# If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
# When a room becomes unused, meetings that have an earlier original start time should be given the room.
# Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

# A half-closed interval [a, b) is the interval between a and b including a and not including b.

class Solution:
    def mostBooked(self, N: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        countMeetings = defaultdict(int)
        avail_rooms = [i for i in range(N)]
        heapq.heapify(avail_rooms)
        heap = []
        for start, end in meetings:
            while heap and heap[0][0] <= start:
                avail_time, n = heapq.heappop(heap)
                heapq.heappush(avail_rooms, n)
            if avail_rooms:
                n = heapq.heappop(avail_rooms)
                heapq.heappush(heap, [end,n])
                countMeetings[n] += 1
            else:
                avail_time, n = heapq.heappop(heap)
                heapq.heappush(heap, [avail_time + end - start, n])
                countMeetings[n] += 1
        maxMeetings = max(countMeetings.values())
        for i in range(N):
            if countMeetings[i] == maxMeetings:
                return i

            