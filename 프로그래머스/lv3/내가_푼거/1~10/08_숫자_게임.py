from collections import deque

def solution(A, B):
    A = sorted(A)
    b_dq = deque(sorted(B))
    score = 0

    while A :
        cur_A = A.pop()

        if b_dq[-1] <= cur_A :
            cur_B = b_dq.popleft()
        else :
            cur_B = b_dq.pop()
            score += 1

    return score

print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))