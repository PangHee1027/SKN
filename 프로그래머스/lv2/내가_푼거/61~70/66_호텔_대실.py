def convert(time_string) :
    hour, minute = map(int, time_string.split(":"))
    return hour * 60 + minute

def solution(book_time):
    converted_book_time = []

    for time in book_time :
        converted_book_time.append([convert(time[0]), convert(time[1]) + 10])
    converted_book_time.sort(key= lambda x : x[0])

    dl = []

    for time in converted_book_time :
        if not dl :
            dl.append([time])
            continue
        for i, pre in enumerate(dl) :
            if pre[-1][1] <= time[0] :
                dl[i].append(time)
                break
        else :
            dl.append([time])

    answer = 0
    return len(dl)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))