class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        visit=set()
        length=0
        while r<len(s):
            while s[r] in visit:
                visit.remove(s[l])
                l+=1
            visit.add(s[r])
            longest= r-l+1
            length= max(length,longest)
            r+=1
        return length

