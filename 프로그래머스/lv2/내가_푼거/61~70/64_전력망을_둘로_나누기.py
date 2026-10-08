from collections import deque

def solution(n, wires):
    answer = n + 1
    dq = deque(wires)

    while dq :
        dq1 = deque(wires)
        cur1, cur2 = dq.popleft()
        set1, set2 = set(), set()
        set1.add(cur1)
        set2.add(cur2)
        while dq1 :
            c1, c2 = dq1.popleft()
            if c1 == cur1 and c2 == cur2 :
                continue
            if c1 in set1 or c2 in set1 :
                set1.add(c1)
                set1.add(c2)
            elif c1 in set2 or c2 in set2 :
                set2.add(c1)
                set2.add(c2)
            else :
                dq1.append([c1, c2])
        answer = min(answer, abs(len(set1) - len(set2)))

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))