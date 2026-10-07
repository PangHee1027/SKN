from collections import deque

def solution(queue1, queue2):
    max_iter = (len(queue1) + len(queue2)) * 2 + 1

    if (sum(queue1) + sum(queue2)) % 2 :
        return -1

    sum1, sum2 = sum(queue1), sum(queue2)
    mean = (sum1 + sum2) // 2
    dq1, dq2 = deque(queue1), deque(queue2)

    for i in range(max_iter) :
        if sum1 == mean :
            return i
        match sum1 < sum2 :
            case True :
                x = dq2.popleft()
                sum2 -= x
                sum1 += x
                dq1.append(x)
            case False :
                x = dq1.popleft()
                sum1 -= x
                sum2 += x
                dq2.append(x)

    return -1

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))