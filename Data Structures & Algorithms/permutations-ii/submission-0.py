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
            for n in count:
                if count[n]>0:
                    sub.append(n)
                    count[n]-=1
                    dfs()
                    count[n]+=1
                    sub.pop()
            return res
        return dfs()


          