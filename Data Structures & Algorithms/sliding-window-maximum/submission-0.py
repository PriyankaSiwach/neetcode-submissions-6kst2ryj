class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q= collections.deque()
        l=r=0
        output=[]

        while r<len(nums):
            while q and nums[q[-1]]<nums[r]: # keep removing from the right
                q.pop()
            q.append(r)

            
            if (r+1)>=k:  #once window size is valid, append 
                output.append(nums[q[0]])
                l+=1
            if l>q[0]: # remove l from window if index is greater and not in window
                q.popleft()
            r+=1
        return output

            


            

        