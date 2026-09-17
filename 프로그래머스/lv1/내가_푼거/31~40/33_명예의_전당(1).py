def solution(k, score):
    list = []
    answer = []

    for i in score :
        list.append(i)
        list.sort(reverse = True)
        list = list[:k]
        answer.append(list[-1])
    return answer

# print(solution(3, [10, 100, 20, 150, 1, 100, 200]))