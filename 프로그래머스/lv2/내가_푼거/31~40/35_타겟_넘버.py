from collections import deque

def solution(numbers, target):
    queue = deque()

    for v in numbers :
        if not len(queue) :
            queue.append(v)
            queue.append(-v)
            continue
        repeat = len(queue)
        for _ in range(repeat) :
            cur = queue.popleft()
            queue.append(cur + v)
            queue.append(cur - v)

    return queue.count(target)

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))