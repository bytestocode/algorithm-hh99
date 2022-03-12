from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        # even_head에 뭐를 담은 적이 없는데?
        odd.next = even_head

        # head에 뭐를 담은 적이 없는데?
        return head


        # 홀수 노드, 짝수 노드를 담을 연결리스트를 각각 만들고
        # 홀수 연결리스트 맨 뒤에 짝수 연결리스트를 연결

        # node = head
        # odd_list = ListNode()
        # even_list = ListNode()
        # idx = 0
        #
        # while node:
        #     # 노드가 홀수인 경우
        #     if idx % 0 == 0:
        #         odd_list.val = node.val
        #         node = node.next
        #         idx += 1
        #     # 노드가 짝수인 경우
        #     else:
        #         even_list.val = node.val
        #         node = node.next
        #         idx += 1
        #
        #
        # return ListNode()
