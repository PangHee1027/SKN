def solution(s):
    last_char = {}
    answer = []

    for i in range(len(s)) :
        if last_char.get(s[i]) == None :
            last_char[s[i]] = i
            answer.append(-1)
        else :
            answer.append(i - last_char[s[i]])
            last_char[s[i]] = i
    return answer

# print(solution("aaaaaaaaa"))