# Linked List

## 1. Linked List Cycle

> Given a linked list, determine if it has a cycle in it.

**Constraints:** 
- The number of the nodes in the list is in the range [0, 104].
- -105 <= Node.val <= 105
- pos is -1 or a valid index in the linked-list.
    
**Follow up:** Can you solve it using O(1) (i.e. constant) memory?

Define a singly linked list

```
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
```

Code to check cycle in linked list use **Hare and Tortoise** algorithm (fast and slow pointers)

```
class Solution:
    def hasCycle(self, head):

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

```

