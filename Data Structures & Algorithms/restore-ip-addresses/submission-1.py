class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        path=[]
        def backtrack(i):
            if len(path)==4 and i==len(s):
                res.append(".".join(path))
                return
            for j in range(i,min(i+3,len(s))):
                part=s[i:j+1]
                if int(part)>255 or (len(part)>1 and part[0]=="0"):
                    break
                path.append(part)
                backtrack(j+1)
                path.pop()
        backtrack(0)
        return res
                
