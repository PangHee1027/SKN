def solution(people, limit):
    remain = sorted(people)
    count = 0
    for n in range(1, len(people) + 1) :
        heavy = remain.pop()
        light = remain[count] if count < len(remain) else 0
        if light > 0 and heavy + light <= limit :
            count += 1
        if count >= len(remain) :
            return n
    
print(solution([70, 80, 50], 100))