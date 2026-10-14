def colatz(num) :
    result = [num]

    while num > 1 :
        if not num % 2 :
            num //= 2
        else :
            num = num * 3 + 1
        result.append(num)

    return result

def integral(colatz_list) :
    result = []
    for a, b in zip (colatz_list, colatz_list[1:]) :
        result.append((a + b) / 2)

    return result

def solution(k, ranges):
    answer = []
    integral_colatz = integral(colatz(k))
    length = len(integral_colatz)
    for a, b in ranges :
        b = length + b
        start, last = min(a, b), max(a, b)
        if a == b :
            answer.append(0.0)
            continue
        cur = sum(integral_colatz[start : last])
        answer.append(-1.0 if a > b else cur)

    return answer

print(solution(5, [[0, 0], [0, -1], [2, -3], [3, -3]]))
print(solution(3, [[0, 0], [1, -2], [3, -3]]))