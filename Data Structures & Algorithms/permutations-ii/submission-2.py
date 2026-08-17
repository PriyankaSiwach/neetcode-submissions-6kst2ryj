class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]
        count={n:0 for n in nums}
        for n in nums:
            count[n]+=1
        def dfs():
            if len(sub)==len(nums):
                res.append(sub[:])
                return
            for i in count:
                if count[i]>0:
                    sub.append(i)
                    count[i]-=1
                    dfs()
                    count[i]+=1
                    sub.pop()
        dfs()
        return res
                    