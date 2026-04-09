class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        l,r=0,0
        res=0
        while r<len(s):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            res= max(res,r-l+1)
            r+=1
        return res

        