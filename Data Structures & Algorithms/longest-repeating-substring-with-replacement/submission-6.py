class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        l=0
        res=0
        for r in range(len(s)):
            c=s[r]
            count[c]=1+count.get(c,0)
            val=(r-l+1)-max(count.values())
            if val<=k:
                res= max(res,r-l+1)
            else:
                count[s[l]]-=1
                l+=1
        return res




