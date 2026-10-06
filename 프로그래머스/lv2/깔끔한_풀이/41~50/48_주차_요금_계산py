import math
from collections import defaultdict

def solution(fees, records):
    dt, df, ut, uf = fees  # 기본시간, 기본요금, 단위시간, 단위요금
    
    in_time = {}                   # 차량별 입차 시각 저장
    total_time = defaultdict(int)  # 차량별 누적 주차 시간
    
    # 1. 입/출차 기록 처리
    for record in records:
        time_str, car, status = record.split()
        h, m = map(int, time_str.split(":"))
        time = h * 60 + m
        
        if status == "IN":
            in_time[car] = time
        else:
            total_time[car] += time - in_time.pop(car)
            
    # 2. 출차 기록이 없는 차량 처리 (23:59 출차 간주)
    max_time = 23 * 60 + 59  # 1439분
    for car, time in in_time.items():
        total_time[car] += max_time - time
        
    # 3. 차량 번호 순으로 주차 요금 계산
    answer = []
    for car in sorted(total_time.keys()):
        time = total_time[car]
        if time <= dt:
            fee = df
        else:
            fee = df + math.ceil((time - dt) / ut) * uf
        answer.append(fee)
        
    return answer