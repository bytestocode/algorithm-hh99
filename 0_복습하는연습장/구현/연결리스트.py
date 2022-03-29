class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, val=0, next=None):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val, None)
