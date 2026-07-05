# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        dummy=ListNode(0)
        nums=set(nums)
        dummy.next=head
        temp=dummy
        temp1=head
        while temp1:
            if temp1.val in nums:
                temp.next=temp1.next
                temp1=temp.next
            else:
                temp=temp.next
                temp1=temp1.next
            
        return dummy.next

            
        
