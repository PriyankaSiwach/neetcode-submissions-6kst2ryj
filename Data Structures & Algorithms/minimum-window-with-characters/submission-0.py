class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT,window={},{}
        if t=="":return ""
        for i in t:
            countT[i]= 1+countT.get(i,0)
        have,need= 0,len(countT)
        l=0
        res,reslen=[-1,-1],float("inf")
        for r in range(len(s)):
            c=s[r]
            window[c]= 1+ window.get(c,0)
            if c in countT and countT[c]==window[c]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1
                window[s[l]]-=1
                if s[l] in countT and countT[s[l]]>window[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen!=float("inf") else ""


        

    

                
