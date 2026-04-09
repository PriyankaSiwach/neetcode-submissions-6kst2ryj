class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda i: i[0])
        output=[intervals[0]]

        for start,end in intervals[1:]:
            lastvalue= output[-1][1]
            if start<=lastvalue:
                output[-1]= [output[-1][0], max(lastvalue,end)]
            else:
                output.append([start, end])
        return output
        

        

        
        