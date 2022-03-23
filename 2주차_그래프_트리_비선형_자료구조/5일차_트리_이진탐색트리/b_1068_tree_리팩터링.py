# 노드의 개수
N = int(input())
# 인덱스: 요소 => 노드: 부모 노드
parent_of_ = list(map(int, input().split()))
# 삭제할 노드
NODE_TO_DELETE = int(input())

# 삭제할 노드를 삭제 리스트에 저장
delete_list = list()
delete_list.append(NODE_TO_DELETE)
# 삭제할 노드의 부모노드 연결 끊기 (의미없는 99 할당)
parent_of_[NODE_TO_DELETE] = 99

# 리스트에 삭제할 노드가 남아 있으면?
while delete_list:
    # 삭제할 노드를 리스트에서 하나 빼냄
    delete = delete_list.pop()
    # 전체 노드를 하나씩 돌면서
    for node in range(len(parent_of_)):
        # 노드의 부모노드가 삭제할 노드인 경우
        if parent_of_[node] == delete:
            # 해당 노드도 삭제 리스트에 저장
            delete_list.append(node)
            # 삭제할 노드의 부모노드 연결 끊기
            parent_of_[node] = 99

# 리프노드 카운트 0으로 초기화
leaf_count = 0
# 전체 노드를 하나씩 돌면서
for node in range(len(parent_of_)):
    # 노드의 부모가 99이면 삭제된 노드라서 continue

    '''
    if parent_of_[node] == -1:
    위 조건식은 넣으면 안됨
    왜냐하면 루트만 남으면 리프노드로 보기 때문!!!
    '''

    if parent_of_[node] == 99:
        continue
    # 노드가 다른 어떤 노드의 부모도 아닌 경우 leaf_count + 1
    if node not in parent_of_:
        leaf_count += 1

# 인덱스: 요소 => 노드: 부모 노드
# print(parent_of_)
# 리프노드의 개수
print(leaf_count)
