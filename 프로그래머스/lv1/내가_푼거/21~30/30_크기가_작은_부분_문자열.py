def solution(t, p):
    sub_length = len(p)
    answer = 0
    for i in range(len(t) - sub_length + 1) :
        if int(p) >= int(t[i: i + sub_length]) :
            answer += 1
    return answer

# print(solution("500220839878", "7"))