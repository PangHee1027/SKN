def calc_time(diff, times, level) :
    result = 0
    for d, t in zip(diff, times):
        result += max(0, d - level) * sum(t) + t[0]
    return result

def solution(diffs, times, limit):
    times_zip = list(zip(times, [0] + times[:-1]))
    a, b = 1, max(diffs)

    while a < b :
        level = (a + b) // 2
        time = calc_time(diffs, times_zip, level)
        if time > limit :
            a = level + 1
        else :
            b = level

    return a

print(solution([1, 5, 3], [2, 4, 7], 30)) # 3
print(solution([1, 4, 4, 2], [6, 3, 8, 2], 59)) # 2
print(solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723)) # 294
print(solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012)) # 39354