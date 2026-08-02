class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        arr=[[] for i in range(len(nums)+1)] 
        res=[]
        for i in nums:
            count[i]= 1+ count.get(i,0)
        for key,val in count.items():
            arr[val].append(key)
        for i in range(len(arr)-1, -1, -1):
            for j in arr[i]:
                res.append(j)
                k-=1
                if k==0:
                    return res


        