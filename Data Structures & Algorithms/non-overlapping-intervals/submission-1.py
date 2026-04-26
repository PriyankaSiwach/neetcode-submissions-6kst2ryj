class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        last=intervals[0][1]
        res=0
        for start,end in intervals[1:]:
            if start>=last:
                last= end
            else:
                res+=1
                last= min(last,end)
        return res


        