from typing import Optional

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None:
            return False

        slow = fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                break

        if fast.next == None or fast.next.next == None:
            return False
        elif fast == slow:
            return True

        return False