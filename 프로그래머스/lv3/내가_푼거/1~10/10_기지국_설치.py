def solution(n, stations, w):
    coverage = []
    answer = 0
    cover = 1 + 2 * w

    for station in stations :
        coverage.append([station - w - 1, station + w + 1])

    start = 1
    end = n

    for e, s in coverage :
        if e < 1 :
            start = s
            continue
        necessary = e - start + 1
        answer += (necessary // cover) + (1 if necessary % cover else 0)
        start = s
        

    if start <= n :
        necessary = n - start + 1
        answer += necessary // cover + (1 if necessary % cover else 0)

    return answer

print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))