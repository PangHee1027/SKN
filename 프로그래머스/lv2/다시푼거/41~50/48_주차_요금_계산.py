from collections import defaultdict

def convert(time) :
    hour, minute = map(int, time.split(':'))
    return hour * 60 + minute

def solution(fees, records) :
    parking_time = defaultdict(list)
    last_time = convert('23:59')
    
    for record in records :
        time, car, io = record.split()
        time = convert(time)
        parking_time[car].append(time if io == 'OUT' else -time)
    
    for k, v in parking_time.items() :
        if len(v) % 2 :
            v.append(last_time)
        v = sum(v)
        fee = fees[1]
        if v <= fees[0] :
            parking_time[k] = fee
            continue
        v -= fees[0]
        fee += ((v + fees[2] - 1) // fees[2]) * fees[3]
        parking_time[k] = fee

    return [x for _, x in sorted(parking_time.items())]