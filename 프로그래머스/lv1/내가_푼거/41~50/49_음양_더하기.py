def solution(absolutes, signs):
    answer = 0
    for num, sign in zip(absolutes, signs) :
        answer += num if sign else -num
    return answer

# print(solution([1,2,3], [False,False,True]))