def convert_time(string) :
    _, time_str, duration_str = string.split()
    h, m, s = time_str.split(':')
    
    # 전부 밀리초(ms) 단위의 정수로 변환
    end_ms = (int(h) * 3600 + int(m) * 60) * 1000 + int(float(s) * 1000)
    
    # 처리시간 T (예: "2.0s")에서 's'를 빼고 밀리초로 변환
    duration_ms = int(float(duration_str[:-1]) * 1000)
    
    # 시작 시간 = 끝 시간 - 처리시간 + 1밀리초 (시작과 끝 포함 조건 반영)
    start_ms = end_ms - duration_ms + 1
    
    return (start_ms, end_ms)

def solution(lines):
    lines = list(map(convert_time, lines))
    answer = 0
    for line in lines :
        start = 0
        end = 0
        for l in lines :
            if line[0] + 1000 > l[0] and line[0] <= l[1] :
                start += 1
            if line[1] + 1000 > l[0] and line[1] <= l[1] :
                end += 1
        answer = max((answer, start, end))

    return answer