# 리스트노드를 생성하는 클래스 정의
class ListNode:
    def __init__(self, val, next):
        # 노드의 값을 할당
        self.val = val
        # 노드의 포인터 지정
        self.next = next


# 연결리스트를 생성하는 클래스 정의
class LinkedList:
    def __init__(self, val=0, next=None):
        self.head = None

    # 연결리스트 맨 뒤에 리스트노드 삽입
    def append(self, val):
        # 연결리스트의 헤드가 없는 경우
        if not self.head:
            # 헤드 리스트노드를 생성
            self.head = ListNode(val, None)
            return

        # 연결리스트의 헤드가 있는 경우
        # 해당하는 헤드를 리스트노드로 지정
        node = self.head
        # 리스트노드의 넥스트가 존재하는경우
        while node.next:
            # 넥스트를 타고타고 다음번 리스트 노드로 넘어감
            node = node.next

        # 더이상 넥스트 리스트노드가 없으면
        # 리스트 노드의 꼬리를 지정
        node.next = ListNode(val, None)
