class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=r=1
        seen={nums[0]}
        while r<len(nums):
            if nums[r] not in seen:
                seen.add(nums[r])
                nums[l]=nums[r]
                l+=1
            r+=1
        return l

        