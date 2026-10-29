def solution(n, t, m, timetable):
    # 1. 시간을 분(minute) 단위로 환산 후 오름차순 정렬
    timetable = sorted([int(x[:2]) * 60 + int(x[3:]) for x in timetable])
    
    # 2. 셔틀 시간대별로 탑승할 크루 리스트 초기화 (09:00 = 540분)
    bus = {540 + i * t: [] for i in range(n)}
    
    # 3. 크루들을 셔틀에 배정
    for time in timetable:
        for bus_time in bus.keys():
            if bus_time >= time and len(bus[bus_time]) < m:
                bus[bus_time].append(time)
                break
                
    # 4. 역순으로 탐색하며 콘이 탈 수 있는 가장 늦은 시간 계산
    for bus_time, people in reversed(bus.items()):
        # 자리가 남았다면 셔틀 도착 시간에 맞춰 타면 됨
        if len(people) < m:
            con_time = bus_time
            break
        # 자리가 꽉 찼다면 마지막 탑승자보다 1분 일찍 도착해야 함
        else:
            con_time = people[-1] - 1
            break
            
    # 5. 분 단위를 "HH:MM" 형식의 문자열로 변환하여 반환
    return f"{con_time // 60:02d}:{con_time % 60:02d}"