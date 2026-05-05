class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts, countT= {},{}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            counts[s[i]]= 1+ counts.get(s[i], 0)
            countT[t[i]]= 1+countT.get(t[i],0)
        for c in counts:
            if counts[c]!=countT.get(c,0):
                return False
        return True
        


        