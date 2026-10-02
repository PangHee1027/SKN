def solution(word) :
    alph_dict = {'A' : 0, 'E' : 1, 'I' : 2, 'O' : 3, 'U' : 4}
    count_dict = {0 : 781, 1 : 156, 2 : 31, 3 : 6, 4 : 1}
    answer = 0
    for i, c in enumerate(word) :
        answer += count_dict[i] * alph_dict[c] + 1
    return answer

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))