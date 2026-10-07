from collections import deque

def solution(queue1, queue2):
    sum1 = sum(queue1)
    total_sum = sum1 + sum(queue2)

    # 전체 합이 홀수면 두 큐의 합을 같게 만들 수 없음
    if total_sum % 2 != 0:
        return -1

    target = total_sum // 2
    dq1 = deque(queue1)
    dq2 = deque(queue2)

    # 원소 교환의 최대 횟수 한계선 (len(queue1) * 4)
    max_iter = len(queue1) * 4

    for i in range(max_iter):
        if sum1 == target:
            return i

        if sum1 < target:
            x = dq2.popleft()
            dq1.append(x)
            sum1 += x
        else:
            x = dq1.popleft()
            dq2.append(x)
            sum1 -= x

    return -1