def string2time(time_string) :
    hour, minute = map(int, time_string.split(":"))
    return hour * 60 + minute

def time2string(time) :
    hour, minute = map(str, divmod(time, 60))
    if len(hour) == 1 :
        hour = '0' + hour
    if len(minute) == 1 :
        minute = '0' + minute
    return hour + ':' + minute

def solution(n, t, m, timetable):
    start_bus = 540
    bus = {start_bus + i * t : [] for i in range(n)}
    timetable = [string2time(x) for x in timetable]
    timetable.sort()

    for time in timetable :
        for bus_time in bus.keys() :
            if bus_time >= time :
                if len(bus[bus_time]) == m :
                    continue
                bus[bus_time].append(time)
                break

    for bus_time, people in reversed(bus.items()) :
        if len(people) < m :
            return time2string(bus_time)
        max_time = people[-1]
        for i in range(m - 1, -1, -1) :
            if max_time > people[i] :
                return time2string(max_time - 1)
        else : 
            return time2string(max_time - 1)
        
    

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])) # "09:00"
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"])) # "09:09"
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])) # "08:59"
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"])) # "00:00"
print(solution(1, 1, 1, ["23:59"])) # "09:00"
print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])) # "18:00"