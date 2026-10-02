from collections import deque

def solution(priorities, location):
    # 1. (원래 인덱스, 우선순위) 형태의 튜플로 deque(큐) 생성
    #    예: priorities가 [2, 1, 3, 2]라면
    #    queue = deque([(0, 2), (1, 1), (2, 3), (3, 2)])
    #    원래 위치(idx)를 함께 저장해두면, 큐 안에서 순서가 섞여도 
    #    목표 프로세스(location)를 수동 인덱스 계산 없이 추적할 수 있습니다.
    queue = deque([(idx, priority) for idx, priority in enumerate(priorities)])
    
    # 실행된 프로세스의 순서를 기록할 변수
    answer = 0

    # 대기 큐에 프로세스가 남아있는 동안 반복 탐색
    while queue:
        # 2. 큐의 맨 앞에 있는 프로세스를 꺼냄
        #    cur[0]: 원래 인덱스, cur[1]: 우선순위
        cur = queue.popleft()
        
        # 3. 큐에 남아있는 프로세스 중 현재 꺼낸 프로세스(cur)보다 우선순위가 높은 것이 있는지 확인
        #    any(...)는 조건식을 만족하는 항목이 1개라도 있으면 True를 반환합니다.
        if any(cur[1] < q[1] for q in queue):
            # 우선순위가 더 높은 프로세스가 큐에 존재하므로 다시 맨 뒤로 넣음
            queue.append(cur)
        else:
            # 4. 더 높은 우선순위가 없으므로 현재 프로세스를 실행시킴
            answer += 1
            
            # 방금 실행된 프로세스(cur[0])가 찾고자 했던 location의 프로세스라면
            # 몇 번째로 실행되었는지(answer) 반환하고 즉시 종료
            if cur[0] == location:
                return answer