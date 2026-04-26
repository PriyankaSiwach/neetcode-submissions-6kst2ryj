class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmax, leftmin=0,0
        for i in s:
            if i=="(":
                leftmax+=1
                leftmin+=1
            elif i==")" :
                leftmax-=1
                leftmin-=1
            else:
                leftmin-=1
                leftmax+=1
            if leftmax<0:
                return False
            if leftmin<0:
                leftmin=0
        return leftmin==0
            

        
        