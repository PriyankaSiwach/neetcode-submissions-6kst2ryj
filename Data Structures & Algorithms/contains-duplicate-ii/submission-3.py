class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visit= set()
        l=0
        for r in range(len(nums)):
            if r-l>k:                ##calculating distance so far
                visit.remove(nums[l]) 
                l+=1
            if nums[r] in visit:    ## this line only reach if dist<k
                return True
            visit.add(nums[r])
        return False
    

        