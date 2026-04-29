class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair: pair[0])

        res = [intervals[0]] # we initialize the res array with a beginning []

        for start, end in intervals:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end) 
            else:
                res.append([start, end])
        return res