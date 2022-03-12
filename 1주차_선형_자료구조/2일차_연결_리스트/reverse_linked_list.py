from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None

        while node:
            next = node.next
            node.next = prev

            prev = node
            node = next

        return prev


        # 리스트(동적 배열)로 변환한 후, 하나씩 팝하면서 연결리스트 만들려고 시도
        # py_list = []
        # node = head
        #
        # while node:
        #     py_list.append(node.val)
        #     node = node.next
        #
        # result = ListNode()
        #
        # while py_list and result:
        #     result.val = py_list.pop()
        #     result.next = ListNode(result.val, ListNode())
        #     result = result.next
        #
        # return result