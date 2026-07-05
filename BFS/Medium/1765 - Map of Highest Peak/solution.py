# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        dummy=ListNode(0)
        dummy.next=list1
        temp1=dummy
        count=0
        while count<a:
            count+=1
            temp1=temp1.next
        temp2=temp1
        while count<=b:
            temp1=temp1.next
            count+=1
        temp2.next=list2
        while temp2.next:
            temp2=temp2.next
        temp2.next=temp1.next
        return dummy.next
