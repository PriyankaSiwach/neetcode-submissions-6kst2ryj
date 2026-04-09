# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy= ListNode(0,head)
        left= dummy
        right=head
        # while n>0 and right:
        #     right=right.next
        #     n-=1
        for _ in range(n):
            right= right.next

        while right:       #once right is at n...start moving left
            left=left.next
            right=right.next
        
        left.next= left.next.next #update pointer
        return dummy.next

         
          


        