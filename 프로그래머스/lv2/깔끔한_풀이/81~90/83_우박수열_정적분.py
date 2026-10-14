def collatz(num):
    result = [num]
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        result.append(num)
    return result

def get_integrals(collatz_list):
    # 리스트 컴프리헨션을 이용해 각 구간의 넓이(사다리꼴 면적) 계산
    return [(a + b) / 2 for a, b in zip(collatz_list, collatz_list[1:])]

def solution(k, ranges):
    answer = []
    integral_colatz = get_integrals(collatz(k))
    length = len(integral_colatz)
    
    for a, b in ranges:
        # 끝점 b를 상대 좌표에서 절대 좌표로 변환
        b = length + b
        start, last = min(a, b), max(a, b)
        
        # 시작점과 끝점이 같은 경우
        if a == b:
            answer.append(0.0)
            continue
            
        # 시작점이 끝점보다 큰 경우 (유효하지 않은 구간)
        if a > b:
            answer.append(-1.0)
            continue
            
        # 정상적인 구간인 경우 정적분 값 계산
        cur = sum(integral_colatz[start:last])
        answer.append(cur)

    return answer