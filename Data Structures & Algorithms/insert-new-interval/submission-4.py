class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):

            # New interval ends before this interval starts
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # New interval begins after this interval ends
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # New interval overlaps with this interval
            else:
                newInterval = [ min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

            
        res.append(newInterval)
        return res