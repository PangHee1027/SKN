def solution(arr):
    a = arr[0]
    cur = a
    answer = 0
    for i in range(1, len(arr)) :
        b = arr[i]
        while b > 0 :
            a, b = b, a % b
        a = cur * arr[i] // a
        cur = a
    return a

print(solution([2,6,8,14]))