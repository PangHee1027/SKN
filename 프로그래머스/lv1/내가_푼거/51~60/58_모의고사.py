def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct = [0, 0, 0]
    for i, v in enumerate(answers) :
        if v == student1[i % 5] :
            correct[0] += 1
        if v == student2[i % 8] :
            correct[1] += 1
        if v == student3[i % 10] :
            correct[2] += 1
    answer = [1]
    max = correct[0]
    for i in range(1,3) :
        if correct[i] == max :
            answer.append(i + 1)
        elif correct[i] > max :
            answer = [i + 1]
            max = correct[i]
    return answer

print(solution([1,3,2,4,2]))