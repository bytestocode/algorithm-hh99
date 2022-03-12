from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)

        return list1


        # 연결리스트의 작은 값부터 하나씩 빼가면서 새로운 연결리스트를 만들려고 함
        # list1_node = list1
        # list2_node = list2
        # result: Optional[ListNode] = ListNode()
        #
        # result.val = 0
        #
        # while list1_node or list2_node:
        #     if list1_node.val < list2_node.val or list1_node.val is None:
        #         result.next = ListNode(val=result.val, next=list1_node.val)
        #         list1_node = list1_node.next
        #     elif list1_node.val > list2_node.val or list2_node.val is None:
        #         result.next = ListNode(val=result.val, next=list2_node.val)
        #         list2_node = list2_node.next
        #     else:
        #         result.next = ListNode(val=result.val, next=list1_node.val)
        #         list1_node = list1_node.next
        #         result.next = ListNode(val=result.val, next=list2_node.val)
        #         list2_node = list2_node.next
        #
        # return result

