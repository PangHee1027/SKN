def solution(n, w, num):
    answer = 1
    a = [i for i in range(1, n + 1)]
    b = [a[i : i + w] for i in range(0, len(a), w)]
    box_list = []
    reverse = False

    for i in range(len(b)) :
        if not reverse :
            if len(b[i]) < w :
                b[i] = b[i] + [0 for i in range(w - len(b[i]))] 
            box_list.append(b[i])
            reverse = not reverse
        else :
            b[i].reverse()
            if len(b[i]) < w :
                b[i] = [0 for i in range(w - len(b[i]))] + b[i]
            box_list.append(b[i])
            reverse = not reverse

    print(box_list)

    for i in range(len(box_list)) :
        for j in range(w) :
            if box_list[i][j] == num :
                answer += len(box_list) - i - 1
                if box_list[len(box_list) - 1][j] == 0 :
                    answer -= 1
    return answer
