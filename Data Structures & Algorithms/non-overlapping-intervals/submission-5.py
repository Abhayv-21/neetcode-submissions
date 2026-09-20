class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0 

        cnt = 0
        intervals.sort(key=lambda x:x[0])
        curr_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < curr_end:
                cnt += 1 
                curr_end = min(curr_end, intervals[i][1])
            else:
                curr_end = intervals[i][1]
        
        return cnt
            