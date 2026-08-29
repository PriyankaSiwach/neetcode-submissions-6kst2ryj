class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total= sum(stones)
        target= (total//2)
        dp={0}
        for stone in stones:
            newdp=set(dp)
            for i in dp:
                if i+stone<=target:
                    
                    newdp.add(i+stone)
                dp=newdp
            best= max(dp)
        return total- 2*best

