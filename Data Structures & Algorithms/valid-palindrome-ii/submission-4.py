class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skipleft=s[l+1:r+1]
                skipright=s[l:r]
                return skipleft==skipleft[::-1] or skipright[::-1]==skipright
            l+=1
            r-=1
        return True
                    