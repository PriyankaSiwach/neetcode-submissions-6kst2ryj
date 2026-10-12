class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort()
        res.append(intervals[0])
        for s,e in intervals[1:]:
            if res[-1][1]>=s:
                start,end= res[-1][0], res[-1][1]
                res.pop()
                res.append([start,max(end,e)])
            else:
                res.append([s,e])
        return res
               