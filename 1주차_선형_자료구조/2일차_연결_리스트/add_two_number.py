from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # 리스트(동적 배열)로 변환하여 계산하고
        # 연결리스트를 만든다

        py_list1 = []
        py_list2 = []
        node1 = l1
        node2 = l2

        while node1:
            py_list1.append(node1.val)
            py_list2.append(node2.val)
            node1 = node1.next
            node2 = node2.next

        py_string_list = py_list1.map()

        num1 = int(''.join(py_list1[::-1]))
        num2 = int(''.join(py_list2[::-1]))
        print(num1, num2)
