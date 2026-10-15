def convert_time(string_time):
    hour, minute = map(int, string_time.split(":"))
    return hour * 60 + minute

def solution(plans):
    # 시간을 분 단위로 변환하고 시작 시각 기준 정렬
    parsed_plans = []
    for subject, start, playtime in plans:
        parsed_plans.append([subject, convert_time(start), int(playtime)])
    parsed_plans.sort(key=lambda x: x[1])

    answer = []
    paused_stack = []  # 잠시 멈춘 과제들을 담을 스택 [subject, remain_time]
    
    current_time = 0
    
    for i in range(len(parsed_plans)):
        sub, start, playtime = parsed_plans[i]
        
        # 현재 과제가 시작하기 전까지 남은 시간 동안 멈춰둔 과제 처리
        while paused_stack and current_time < start:
            paused_sub, paused_remain = paused_stack[-1]
            time_gap = start - current_time
            
            if paused_remain <= time_gap:
                # 남은 시간 안에 멈춘 과제를 끝낼 수 있는 경우
                current_time += paused_remain
                paused_stack.pop()
                answer.append(paused_sub)
            else:
                # 남은 시간 동안 최대한 하고 다시 멈춰야 하는 경우
                paused_stack[-1][1] -= time_gap
                current_time = start
                break
        
        # 현재 시각을 새 과제 시작 시각으로 동기화
        current_time = max(current_time, start)
        
        # 다음 과제가 있거나 마지막 과제일 때 처리
        # 다음 과제 시작 시각 전까지 현재 과제를 끝낼 수 있는지 확인
        if i + 1 < len(parsed_plans):
            next_start = parsed_plans[i + 1][1]
            time_available = next_start - current_time
            
            if playtime <= time_available:
                # 현재 과제를 끝낼 수 있는 경우
                current_time += playtime
                answer.append(sub)
            else:
                # 다 못 끝내고 멈춰야 하는 경우
                playtime -= time_available
                paused_stack.append([sub, playtime])
                current_time = next_start
        else:
            # 마지막 과제인 경우 무조건 끝까지 진행
            answer.append(sub)
            current_time += playtime

    # 남아있는 멈춘 과제들을 최근 순서대로 모두 처리
    while paused_stack:
        answer.append(paused_stack.pop()[0])

    return answer