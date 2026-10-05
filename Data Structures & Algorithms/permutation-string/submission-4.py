class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        counts1,counts2=[0]*26, [0]*26
        l=0
        for c in range(len(s1)):
            counts1[ord(s1[c])-ord('a')]+=1
            counts2[ord(s2[c])-ord('a')]+=1
        if counts1==counts2:
            return True
        for r in range(len(s1),len(s2)):
            c=s2[r]
            counts2[ord(c)-ord('a')]+=1
            counts2[ord(s2[r-len(s1)])-ord('a')]-=1
            if counts1==counts2:
                return True
        return False

            

