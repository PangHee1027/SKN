def solution(left, right):
    answer = 0
    for i in range(left, right + 1) :
        target = int(i ** 0.5) + 1
        count = 0
        for j in range (1, target) :
            if i % j == 0 :
                count += 1 
                if j < i // j :
                    count += 1
        answer += i if count % 2 == 0 else -i
    return answer

# print(solution(24, 27))