def convert_time(time) :
    hour, minute = divmod(time, 100)
    return hour * 60 + minute

def solution(schedules, timelogs, startday) :
    answer = 0
    for schedule, timelog in zip(schedules, timelogs) :
        limit = convert_time(schedule) + 10
        for i, time in enumerate(timelog) :
            today = (startday + i) % 7
            if today == 6 or today == 0 :
                continue
            if convert_time(time) > limit :
                break
        else :
            answer += 1
    return answer