# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        temp=node
        temp.val=temp.next.val
        temp.next=temp.next.next

        
