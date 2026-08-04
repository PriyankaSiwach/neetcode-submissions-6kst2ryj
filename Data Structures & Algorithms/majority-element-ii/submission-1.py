class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=defaultdict()
        n= len(nums)//3
        res=set()

        for i in nums:
            count[i]= 1+ count.get(i,0)
        for i,j in count.items():
            if count[i]>n:
                res.add(i)
        return list(res)