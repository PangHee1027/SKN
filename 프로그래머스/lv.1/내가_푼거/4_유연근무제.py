def solution(schedules, timelogs, startday):
    answer = 0
    today = startday
    for i in range(len(schedules)) :
        time = schedules[i] // 100
        minuite = schedules[i] % 100
        if minuite >= 50 :
            time += 1
            minuite -= 50
        else :
            minuite += 10
        schedules[i] = time * 100 + minuite
        for j in timelogs[i] :
            if j > schedules[i] and today <= 5 :
                today = startday
                break
            today = (1 if today == 7 else (today + 1))
        else :
            today = startday
            answer += 1

    return answer

print(solution([700, 800, 1100], [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]], 5))
