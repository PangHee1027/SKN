def solution(n, arr1, arr2):
    answer = []
    for n1, n2 in zip(arr1, arr2) :
        a = n1 | n2
        result = ''.join('#' if i == '1' else ' ' for i in bin(a)[2:].zfill(n))
        answer.append(result)
    return answer