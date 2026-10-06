class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        count,window={},{}
        res=[-1,-1]
        reslen=float("inf")
        for i in t:
            count[i]=1+count.get(i,0)
        have,need=0,len(count)
        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]= 1+window.get(c,0)
            if c in count and window[c]==count[c]:
                have+=1
            while have==need:
                if reslen> (r-l+1):
                    res=[l,r]
                    reslen= r-l+1
                window[s[l]]-=1
                if s[l] in count and window[s[l]]<count[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen!=float("inf") else ""



            