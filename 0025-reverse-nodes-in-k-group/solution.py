class Solution(object):
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head

        a = 0
        prev = None
        cur = head

        dummy = ListNode(0)
        t2 = dummy

        while cur:
            a += 1
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

            if a == k:
                while prev:
                    t2.next = prev
                    t2 = t2.next
                    prev = prev.next
                a = 0

        # reverse back remaining (<k) nodes
        a = None
        current = prev
        while current:
            nxt = current.next
            current.next = a
            a = current
            current = nxt

        if a:
            t2.next = a

        return dummy.next

