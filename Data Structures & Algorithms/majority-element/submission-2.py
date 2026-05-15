class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count= {}
        key,maxcount= None,0

        for i in nums:
            count[i]= 1+ count.get(i,0)
        for i, c in count.items():
            if c>maxcount:
                maxcount=c
                key=i
        return key
        