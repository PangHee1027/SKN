def solution(arr, divisor) :
    answer = sorted([x for x in arr if not x % divisor])
    return answer if answer else [-1]