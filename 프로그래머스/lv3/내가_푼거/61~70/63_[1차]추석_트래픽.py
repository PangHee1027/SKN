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
    parsed_lines = [convert_time(line) for line in lines]
    max_traffic = 0
    
    for l_start, l_end in parsed_lines:
        # 1. 이 로그의 '시작 시간(l_start)'을 구간의 시작으로 잡을 때 (구간: [l_start, l_start + 1000))
        count1 = 0
        for target_start, target_end in parsed_lines:
            if target_end >= l_start and target_start < l_start + 1000:
                count1 += 1
                
        # 2. 이 로그의 '끝 시간(l_end)'을 구간의 시작으로 잡을 때 (구간: [l_end, l_end + 1000))
        count2 = 0
        for target_start, target_end in parsed_lines:
            if target_end >= l_end and target_start < l_end + 1000:
                count2 += 1
                
        max_traffic = max(max_traffic, count1, count2)

    return max_traffic

print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))