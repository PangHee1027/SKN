def solution(n, lost, reserve):
    students = [1 if i + 1 not in lost else 0 for i in range(n)]
    print(students)
    for i, s in enumerate(students) :
        if s == 0 :
            if i + 1 in reserve :
                students[i] = 1
                reserve.remove(i + 1)
            elif i in reserve :
                students[i] = 1
                reserve.remove(i)
            elif i + 1 < len(students) and i + 2 in reserve and students[i + 1] == 1:
                students[i] = 1
                reserve.remove(i + 2)
            print(students)
    answer = sum(students)
    return answer

# print(solution(5, [4, 2], [3, 5]))