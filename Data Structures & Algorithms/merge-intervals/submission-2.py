class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        result = []

        curr = intervals[0]
        curr_start = curr[0]
        curr_end = curr[1]

        for i in range(len(intervals)):
            if intervals[i][0] <= curr_end:
                curr_end = max(curr_end, intervals[i][1])
            else:
                result.append([curr_start, curr_end])
                curr_start = intervals[i][0]
                curr_end = intervals[i][1]

        # if curr not in result:
        result.append([curr_start, curr_end])

        return result