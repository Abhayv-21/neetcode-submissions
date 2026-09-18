class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = newInterval[0]
        end = newInterval[1]
        result = []

        for i in range(len(intervals)):
            if intervals[i][0] > end:
                result.append([start, end])
                result.extend(intervals[i:])
                return result
            elif intervals[i][1] < start:
                result.append(intervals[i])
            else:
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])

        if newInterval not in result:
            result.append([start, end])

        return result