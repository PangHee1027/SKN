def solution(progresses, speeds):
    require = []
    for i, p in enumerate(progresses) :
        require.append((100 - p) // speeds[i] + (1 if (100-p) % speeds[i] else 0))
    stack = require
    answer = []
    cur = 0
    now = require[0]
    for i in range(len(require)) :
        cur += 1
        if i == len(require) - 1 :
            answer.append(cur)
            break
        if require[i + 1] <= now :
            continue
        else :
            answer.append(cur)
            cur = 0
            now = require[i + 1]

    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))