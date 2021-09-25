"""

Maximum Number of Events That Can Be Attended
 
Given an array of events where events[i] = [startDayi, endDayi]. 
Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. 
Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend.

Example 1:

Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4

Example 3:

Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4

Example 4:

Input: events = [[1,100000]]
Output: 1

Example 5:

Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
Output: 7

Constraints:

1 <= events.length <= 105
events[i].length == 2
1 <= startDayi <= endDayi <= 105

"""

"""

#1. Sort the events based on starting day of the event
#2. Now once you have this sorted events, every day check what are the events that can start today
#3. for all the events that can be started today, keep their ending time in heap.
# - Wait why we only need ending times ?
# i) from today onwards, we already know this event started in the past and all we need to know is when this event will finish
# ii) Also, another key to this algorithm is being greedy, meaning I want to pick the event which is going to end the soonest.
# - So how do we find the event which is going to end the soonest?
# i) brute force way would be to look at all the event's ending time and find the minimum, this is probably ok for 1 day but as we can only attend 1 event a day,
# we will end up repeating this for every day and that's why we can utilize heap(min heap to be precise) to solve the problem of finding the event with earliest ending time
#4. There is one more house cleaning step, the event whose ending time is in the past, we no longer can attend those event
#5. Last but very important step, Let's attend the event if any event to attend in the heap.


"""


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        total_days = max(end for start, end in events)
        day = 0
        event_id = 0
        num_events_attended = 0
        min_heap = []
        
        for day in range(1, total_days+1):
            # Add all the events that start today
            while event_id < len(events) and events[event_id][0] == day:
                heappush(min_heap, events[event_id][1])
                event_id += 1
            
            # Remove all the events whose end date was before today
            while min_heap and min_heap[0] < day:
                heappop(min_heap)
            
            # if any event that can be attended today, let's attend it
            
            if  min_heap:
                heappop(min_heap)
                num_events_attended += 1
                
        return num_events_attended