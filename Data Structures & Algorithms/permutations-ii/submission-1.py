class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]
        visit=set()
        def dfs():
            if len(sub)==len(nums):
                res.append(sub[:])
                return
            used=set()
            for i,v in enumerate(nums):
                if i in visit:
                    continue
                if v in used:
                    continue
                sub.append(v)
                visit.add(i)
                used.add(v)
                dfs()
                visit.remove(i)
      
                sub.pop()
        dfs()
        return res