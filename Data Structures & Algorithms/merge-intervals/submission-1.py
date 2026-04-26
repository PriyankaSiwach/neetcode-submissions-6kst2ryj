class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda i: i[0])
        output=[intervals[0]]

        for start, end in intervals[1:]:
            last= output[-1]
            if start<=last[1]:
                output[-1]= [output[-1][0],max(last[1],end)]
            else:
                output.append([start,end])
        return output
        


        

        

        
        