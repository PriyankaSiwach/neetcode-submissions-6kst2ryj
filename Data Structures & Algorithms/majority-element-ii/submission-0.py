class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        res=[]
        for i in nums:
            count[i]= 1+ count.get(i, 0)
        t= len(nums)//3
        for x,c in count.items():
            if c > t:
                res.append(x)
        return res
        