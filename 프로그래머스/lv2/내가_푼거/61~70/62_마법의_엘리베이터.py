def solution(storey):
    answer = 0
    while storey > 0 :
        storey, cur = storey // 10, storey % 10
        if cur < 5 :
            answer += cur
        elif cur > 5 :
            answer += 10 - cur
            storey += 1
        else :
            if storey % 10 >= 5 :
                storey += 1
            answer += 5
    return answer

print(solution(16))
print(solution(2554))