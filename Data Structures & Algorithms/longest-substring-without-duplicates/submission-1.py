class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit= set()
        l,r= 0,0
        length=0
        while r<len(s):
            while s[r] in visit:
                visit.remove(s[l])
                l+=1
            visit.add(s[r])
            length= max(length, r-l+1)
            r+=1
        return length
        
        