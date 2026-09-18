"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x:x.start)

        room = 1
        minheap = [] 
        
        heapq.heappush(minheap, intervals[0].end)

        for i in range(1, len(intervals)):
            if intervals[i].start >= minheap[0]:
                heapq.heappop(minheap)
            heapq.heappush(minheap, intervals[i].end)
            room = max(room, len(minheap))

        return room