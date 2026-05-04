class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2   # sum of 0 to n
        actual = sum(nums)             # sum of what we have
        return expected - actual
  
        
        