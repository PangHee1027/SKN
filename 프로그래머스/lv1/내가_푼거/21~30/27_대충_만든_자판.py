def solution(keymap, targets):
    answer = []
    key_dict = {}

    for i in keymap :
        for j in range(len(i)) :
            if not key_dict.get(i[j]) :
                key_dict[i[j]] = j + 1
            elif key_dict.get(i[j]) > j :
                key_dict[i[j]] = j + 1

    for i in targets :
        now = 0
        for j in i :
            if key_dict.get(j) :
                now += key_dict[j]
            else :
                answer.append(-1)
                break
        else :
            answer.append(now)

    return answer

# print(solution(["AA"], ["B"]))