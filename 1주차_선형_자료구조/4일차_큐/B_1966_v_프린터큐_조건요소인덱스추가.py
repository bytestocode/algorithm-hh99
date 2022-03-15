# N = 3
#
# 문서의 개수 / 인쇄된 순서가 궁금한 문서 = 1 / 0
# N개 문서의 중요도 = 5
# 정답 = 1
#
# 문서의 개수 / 인쇄된 순서가 궁금한 문서 = 4 / 2
# N개 문서의 중요도 = 1 2 3 4
# 정답 2
#
# 문서의 개수 / 인쇄된 순서가 궁금한 문서 = 6 / 0
# N개 문서의 중요도 = 1 1 9 1 1 1
# 정답 5


from collections import deque

# q_deque = deque([5])
q_deque = deque([1, 2, 3, 4])
# q_deque = deque([1, 1, 9, 1, 1, 1])

# q_order_idx = 0
q_order_idx = 2
# q_order_idx = 0

# 출력 횟수 카운트
count = 0

max_num = max(list(q_deque))

# 첫번째 숫자의 최댓값 여부 확인
while True:
    print('1. while 답 찾을 때까지 돌리기')
    if q_order_idx == 0:
        print('2-A. if 정답 찾는 요소 == 첫번째에 있으면')
        # 첫번째 값이 max 이면?
        if q_deque[0] == max_num:
            print('3-A. if 첫번째 요소 == 최댓값')
            print(f'!! 정답 찾는 요소의 출력 순서: {count + 1}')
            break
        else:
            print('3-B. if 첫번째 요소 != 최댓값')
            q_order_idx = len(q_deque) - 1 if q_order_idx - 1 < 0 else q_order_idx - 1
            q_deque.append(q_deque.popleft())
            print(f'4. 현재 데크: {q_deque}')
            print(f'5. 현재 인덱스: {q_order_idx}, 카운트: {count}')
            print('')

    else:
        print('2-B. if 정답 찾는 요소 == 첫번째 아니면')
        if q_deque[0] == max(list(q_deque)):
            print('3-A. if 첫번째 요소 == 최댓값')
            q_deque.popleft()
            max_num = max(list(q_deque))
            q_order_idx = q_order_idx - 1
            count += 1
            print(f'4. 현재 데크: {q_deque}')
            print(f'5. 현재 인덱스: {q_order_idx}, 카운트: {count}')
            print('')
        else:
            print('3-B. if 첫번째 요소 != 최댓값')
            q_order_idx = q_order_idx - 1
            q_deque.append(q_deque.popleft())
            print(f'4. 현재 데크: {q_deque}')
            print(f'5. 현재 인덱스: {q_order_idx}, 카운트: {count}')
            print('')
