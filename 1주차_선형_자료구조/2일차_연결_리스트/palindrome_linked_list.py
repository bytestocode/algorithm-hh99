from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        py_list = []
        node = head

        while node:
            py_list.append(node.val)
            node = node.next

        print(py_list)

        left = 0
        right = len(py_list) - 1
        while py_list[left] == py_list[right]:
            if left < right:
                left += 1
                right -= 1
            else:
                return True

        return False
