class Solution(object):
    def isPalindrome(self, head):
        slow=head
        fast=head
        if head is None or head.next is None:
            return True
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        if fast:
            slow=slow.next
        

        prev=None
        curr=slow
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        temp=head
        bo=True
        while prev:
            if prev.val!=temp.val:
                bo=False
                break
            prev=prev.next
            temp=temp.next
        if bo:
            return True
        else:
            return False

        
        
