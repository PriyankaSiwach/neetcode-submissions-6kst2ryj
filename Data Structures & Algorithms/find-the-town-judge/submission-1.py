class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming= defaultdict(int)
        outgoing=defaultdict(int)
        for i,j in trust:
            incoming[j]+=1
            outgoing[i]+=1
        for i in range(1,1+n):
            if incoming[i]==n-1 and outgoing[i]==0:
                return i
        return -1


