def convert_time(str_time) :
    hour, minute, second = map(int, str_time.split(':'))
    return hour * 3600 + minute * 60 + second

def solution(play_time, adv_time, logs):
    play_time, adv_time = convert_time(play_time), convert_time(adv_time)
    play_time
    play_time_prefix = [0] * (play_time + 2)
    for log in logs :
        log = log.split('-')
        log_start, log_end = convert_time(log[0]), convert_time(log[1])
        play_time_prefix[log_start] += 1
        play_time_prefix[log_end] -= 1

    for i in range(1, play_time + 2):
        play_time_prefix[i] += play_time_prefix[i - 1]
    for i in range(1, play_time + 2):
        play_time_prefix[i] += play_time_prefix[i - 1]

    best_time = 0
    max_people = 0

    for start_time in range(0, play_time - adv_time + 1):
        end_time = start_time + adv_time

        cur_people = play_time_prefix[end_time - 1]

        if start_time > 0:
            cur_people -= play_time_prefix[start_time - 1]

        if cur_people > max_people:
            best_time = start_time
            max_people = cur_people

    hour = best_time // 3600 
    minute = (best_time % 3600) // 60
    second = (best_time) % 60
    return str(hour).zfill(2) + ':' + str(minute).zfill(2)  + ':' + str(second).zfill(2) 

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"])) # "01:30:59"
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])) # "01:00:00"
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])) # "00:00:00"