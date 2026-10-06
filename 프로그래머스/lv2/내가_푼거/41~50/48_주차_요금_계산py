import math

def solution(fees, records):
    def convert_time(time) :
        hour, minute = time.split(":")
        return int(hour) * 60 + int(minute)
    
    parcking_info = {}
    parcking_time = {}
    parcking_cars = set()
    for info in records :
        info_splited = info.split(" ")
        parcking_cars.add(info_splited[1])
        if parcking_info.get(info_splited[1], 0) :
            parcking_info[info_splited[1]].append(convert_time(info_splited[0]))
        else :
            parcking_info[info_splited[1]] = [convert_time(info_splited[0])]
    parcking_cars = list(parcking_cars)
    parcking_cars.sort()

    for car, times in parcking_info.items() :
        for i in range(len(times) // 2) :
            if parcking_time.get(car, 0) :
                parcking_time[car] += parcking_info.get(car)[i * 2 + 1] - parcking_info.get(car)[i * 2]
            else : 
                parcking_time[car] = parcking_info.get(car)[i * 2 + 1] - parcking_info.get(car)[i * 2]
        if len(times) % 2 :
            if  parcking_time.get(car, 0) :
                parcking_time[car] += convert_time("23:59") - parcking_info.get(car)[-1]
            else :
                parcking_time[car] = convert_time("23:59") - parcking_info.get(car)[-1]

    answer = []

    for car in parcking_cars :
        time = parcking_time[car]
        if time < fees[0] :
            answer.append(fees[1])
            continue
        answer.append(fees[1] + (math.ceil((time - fees[0]) / fees[2])) * fees[3])
    
    return answer

# print(solution([180, 5000, 10, 600],
#              ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))