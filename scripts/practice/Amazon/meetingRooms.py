"""

Meeting Rooms II

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106

"""

# Priority Queues

"""

Algorithm

- Sort the given meetings by their start time.
- Initialize a new min-heap and add the first 
meeting's ending time to the heap. We simply need to 
keep track of the ending times as that tells us when 
a meeting room will get free.
- For every meeting room check if the minimum element 
of the heap i.e. the room at the top of the heap is free or not.
- If the room is free, then we extract the topmost element and 
add it back with the ending time of the current meeting we are processing.
- If not, then we allocate a new room and add it to the heap.
- After processing all the meetings, the size of the heap will 
tell us the number of rooms allocated. This will be the minimum 
number of rooms needed to accommodate all the meetings.

"""

"""

Complexity Analysis

Time Complexity: O(NlogN)

There are two major portions that take up time here. 
One is sorting of the array that takes O(NlogN) 
considering that the array consists of N elements.

Then we have the min-heap. In the worst case, all N meetings 
will collide with each other. In any case we have N add operations on the heap. 
In the worst case we will have NN extract-min operations as well. 
Overall complexity being (NlogN) since extract-min operation 
on a heap takes O(logN).

Space Complexity: O(N) because we construct the min-heap and 
that can contain N elements in the worst case as described above 
in the time complexity section. Hence, the space complexity is O(N).

"""




import heapq
class Solution:
    def minMeetingRooms(self, intervals):

        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key=lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)


# Chronological Ordering

"""

Algorithm

- Separate out the start times and the end 
times in their separate arrays.
- Sort the start times and the end times separately. 
Note that this will mess up the original correspondence 
of start times and end times. They will be treated individually now.
- We consider two pointers: s_ptr and e_ptr which 
refer to start pointer and end pointer. The start 
pointer simply iterates over all the meetings and 
the end pointer helps us track if a meeting has 
ended and if we can reuse a room.
- When considering a specific meeting pointed 
to by s_ptr, we check if this start timing is 
greater than the meeting pointed to by e_ptr. 
If this is the case then that would mean some 
meeting has ended by the time the meeting at 
s_ptr had to start. So we can reuse one of the rooms. 
Otherwise, we have to allocate a new room.
- If a meeting has indeed ended i.e. if start[s_ptr] >= end[e_ptr], then we increment e_ptr.
- Repeat this process until s_ptr processes all of the meetings.

"""

"""

Complexity Analysis

Time Complexity: O(NlogN) because all we are doing is 
sorting the two arrays for start timings and end timings 
individually and each of them would contain N elements 
considering there are N intervals.

Space Complexity: O(N) because we create two separate 
arrays of size N, one for recording the start times and one for the end times.

"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1
            start_pointer += 1

        return used_rooms
