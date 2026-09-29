def solution(array, commands):
    answer = []
    for start, last, index in commands :
        arr = array[start - 1 : last]
        arr.sort()
        answer.append(arr[index - 1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))