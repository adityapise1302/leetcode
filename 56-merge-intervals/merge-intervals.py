class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        def overlap(a: List[int], b: List[int]):
            return not (a[1] < b[0] or b[1] < a[0])
        res = []
        for interval in intervals:
            if not res or not overlap(res[-1], interval):
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res