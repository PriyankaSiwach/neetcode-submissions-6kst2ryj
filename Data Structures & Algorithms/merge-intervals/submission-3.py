class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        arr=[intervals[0]]
        for s,e in intervals[1:]:
            if s<=arr[-1][1]:
                arr[-1]= [arr[-1][0], max(arr[-1][1],e)]
            else:
                arr.append([s,e])
        return arr


