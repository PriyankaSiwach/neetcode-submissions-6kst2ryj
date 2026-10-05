class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit=set()
        l=0
        reslen=0
        for r in range(len(s)):
            c=s[r]
            while c in visit:
                visit.remove(s[l])
                l+=1
            reslen= max(reslen, r-l+1)
            visit.add(c)
        return reslen