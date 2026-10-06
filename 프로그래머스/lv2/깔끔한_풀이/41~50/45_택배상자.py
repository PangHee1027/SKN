def solution(order):
    stack = []
    curr_box = 1  # 메인 컨테이너 벨트에서 넘어오는 상자 번호 (1번부터 시작)
    answer = 0
    
    for hope in order:
        # 1. 원하는 상자(hope)가 나올 때까지 메인 컨테이너 상자들을 스택에 보관
        while curr_box <= len(order) and curr_box <= hope:
            stack.append(curr_box)
            curr_box += 1
            
        # 2. 보조 컨테이너(스택)의 맨 위 상자가 원하는 상자인지 확인
        if stack and stack[-1] == hope:
            stack.pop()
            answer += 1
        else:
            # 보조 컨테이너에서도 상자를 꺼낼 수 없다면 더 이상 싣지 못함
            break
            
    return answer