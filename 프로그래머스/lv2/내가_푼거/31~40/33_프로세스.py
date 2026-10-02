def solution(priorities, location):
    answer = 1
    while True :
        cur = priorities.pop(0)
        if not priorities :
            return answer
        if cur >= max(priorities) :
            if not location :
                return answer
            answer += 1
        else :
            priorities.append(cur)
        if not location :
            location = len(priorities)
        location -= 1

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))