def solution(progresses, speeds):
    # 1. 각 작업당 완료까지 필요한 일수 계산 (음수 나눗셈으로 올림 처리)
    days = [-((p - 100) // s) for p, s in zip(progresses, speeds)]
    
    answer = []
    now = days[0]
    cur = 0
    
    # 2. 순차적으로 배포 그룹 카운팅
    for day in days:
        if day <= now:
            cur += 1
        else:
            answer.append(cur)
            now = day
            cur = 1
            
    # 마지막 배포 그룹 추가
    answer.append(cur)
    
    return answer