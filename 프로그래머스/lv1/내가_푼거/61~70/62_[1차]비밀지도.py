import numpy as np

def solution(n, arr1, arr2):
    map = []
    for num1, num2 in zip(arr1, arr2) :
        current1 = []
        current2 = []
        while num1 > 0 :
            current1.append(num1 % 2)
            num1 = num1 // 2
        while len(current1) < n :
            current1.append(0)
        current1.reverse()
        while num2 > 0 :
            current2.append(num2 % 2)
            num2 = num2 // 2
        while len(current2) < n :
            current2.append(0)
        current2.reverse()
        map.append(np.array(current1) + np.array(current2))
    answer = []
    for i in map :
        current = ""
        for j in i :
            if j == 0 :
                current += " "
            else :
                current += "#"
        answer.append(current)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
