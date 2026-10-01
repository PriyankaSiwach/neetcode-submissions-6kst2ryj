class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        sub=[]
        def back(v):
            if len(sub)==k:
                res.append(sub[:])
                return
            for i in range(v,n+1):
                if i in sub:
                    continue
                sub.append(i)
                back(i+1)
                sub.pop()
        back(1)
        return res


